import numpy as np
import matplotlib.pyplot as plt
import time

debug_print = False


def time_to_string_hh_mm_ss(s):
    ss = s%60
    mm = int(s // 60)
    hh = int(mm // 60)
    if hh > 0:
        return (str(hh) + ' h, ' + str(mm) + ' min, ' +str(int(ss)) + ' sec.')
    elif mm > 0:
        return (str(mm) + ' min, ' +str(int(ss)) + ' sec.')
    else:
        return (str(int(ss)) + ' sec.')

def load_geometry(filename):
    img = plt.imread(filename)
    den = np.transpose(img[:,:,0].astype(float)) + 1.
    den /= np.amax(den)
    den = 1. - den + 0.01
    xgrid = np.linspace(0., float(len(den[:,0])),len(den[:,0])+1)
    ygrid = np.linspace(0., float(len(den[0,:])),len(den[0,:])+1)
    bbox = np.array([[-1000., 1000.],[-1000., 1000.]])
    geom = (xgrid, ygrid, den, bbox)
    return geom

def initialize_particles(n, x0, y0, angle0, divergence):
    pos = np.ones((n,2))
    pos[:,0] = x0
    pos[:,1] = y0

    #angle = angle0 * np.ones(n) + (0.5 - np.random.ranf(n)) * divergence
    angle = angle0 * np.ones(n) + (np.random.normal(0.0, 1.0, n)) * divergence/2.0
    #angle = 2. * np.pi * np.random.ranf(n)# ( (7./8.) - 1./16. + 1./8 * np.random.ranf(n))
    return (pos, angle)

def ray_trace_outside(pos, angle, geom):
    if debug_print:
        print('o')
    vx = np.cos(angle)
    vy = np.sin(angle)
    x0 = pos[0]
    y0 = pos[1]
    xmin = geom[0][0]
    xmax = geom[0][-1]
    ymin = geom[1][0]
    ymax = geom[1][-1]
    bbox = geom[3]

    if debug_print:
        print('x, y = ',end='')
        print(x0,y0)
        print('vx, vy = ',end='')
        print(vx,vy)

    if x0 < xmin:
        x1 = xmin + 1.e-8
        if vx * (x1 - x0) > 0.:
            y1 = vy/vx * (x1 - x0) + y0
            if y1 < ymax and y1 > ymin:
                return np.array((x1,y1))
    if x0 > xmax:
        x1 = xmax - 1.e-8
        if vx * (x1 - x0) > 0.:
            y1 = vy/vx * (x1 - x0) + y0
            if y1 < ymax and y1 > ymin:
                return np.array((x1,y1))
    if y0 < ymin:
        y1 = ymin + 1.e-8
        if vy * (y1 - y0) > 0.:
            x1 = vx/vy * (y1 - y0) + x0
            if x1 < xmax and x1 > xmin:
                return np.array((x1,y1))
    if y0 > ymax:
        y1 = ymax - 1.e-8
        if vy * (y1 - y0) > 0.:
            x1 = vx/vy * (y1 - y0) + x0
            if x1 < xmax and x1 > xmin:
                return np.array((x1,y1))


    # x boundary
    dx = bbox[0, int(np.sign(vx)*0.5 + 0.5)] - x0 + np.sign(vx) * 1.e-8
    # y boundary
    dy = bbox[1, int(np.sign(vy)*0.5 + 0.5)] - y0 + np.sign(vy) * 1.e-8
    if debug_print:
        print('dx, dy = ',end='')
        print(dx,dy)
        print('vx/vy * dy, vy/vx * dx = ',end='')
        print(vx/vy * dy,vy/vx * dx)
    if abs(vx/vy * dy) < abs(dx):
        dx = vx/vy * dy
    else:
        dy = vy/vx * dx
    if debug_print:
        print('dx_, dy_ = ',end='')
        print(dx,dy)    #dx = min(dx, dy * vx/vy)
    x1 = x0 + dx
    y1 = y0 + dy

    return np.array((x1,y1))

def distance_in_mfp(dist, st, density):
    return dist *  (np.exp(6. * density) - 0.99) * st

def ray_trace_inside(pos, angle, geom, L, st):
    if debug_print:
        print('i')
    x = pos[0]
    y = pos[1]
    x_ = int(x)
    y_ = int(y)
    xgrid = geom[0]
    ygrid = geom[1]
    density = geom[2]

    vx = np.cos(angle)
    vy = np.sin(angle)
    d = 0. #distance traveled so far in units of mean free path

    while d < L:
        if debug_print:
            print('x, y = ',end='')
            print(x,y)
            print('vx, vy = ',end='')
            print(vx,vy)
        # find next cell boundary to hit
        # x boundary
        #print(x,y,vx,vy)
        dx = xgrid[x_ + int(np.sign(vx)*0.5 + 0.5)] - x + np.sign(vx) * 1.e-8
        # y boundary
        dy = ygrid[y_ + int(np.sign(vy)*0.5 + 0.5)] - y + np.sign(vy) * 1.e-8
        #dx = min(dx, dy * vx/vy)
        #dy = dx * vy/vx
        if abs(vx/vy * dy) < abs(dx):
            dx = vx/vy * dy
        else:
            dy = vy/vx * dx
        dd = np.sqrt(dx*dx + dy*dy)
        dd_in_mfp = distance_in_mfp(dd, st, density[x_,y_])
        if d + dd_in_mfp > L:
            dx *= (L-d)/dd_in_mfp
            dy *= (L-d)/dd_in_mfp
            d = L
        else:
            d += dd_in_mfp
        x += dx
        y += dy
        x_ = int(x)
        y_ = int(y)

        if is_outside_scoring_region(np.array([x,y]),geom):
            break

    return np.array([x,y])

def is_outside_bbox(pos, geom):
    if pos is None:
        return True
    else:
        bbox = geom[3]
        return pos[0] < bbox[0,0] or pos[0] > bbox[0,1] or pos[1] < bbox[1,0] or pos[1] > bbox[1,1]

def is_outside_scoring_region(pos, geom):
    if pos is None:
        return True
    else:
        x = pos[0]
        y = pos[1]
        xgrid = geom[0]
        ygrid = geom[1]
        return x < xgrid[0] or x > xgrid[-1] or y < ygrid[0] or y > ygrid[-1]

def is_inside_bbox(pos, geom):
    return not is_outside_bbox(pos, geom)

def is_inside_scoring_region(pos, geom):
    return not is_outside_scoring_region(pos, geom)

def transport_until_next_collision(pos, angle, geom, st):
    if debug_print:
        print('t')
    x = pos[0]
    y = pos[1]
    xgrid = geom[0]
    ygrid = geom[1]
    L = -np.log(np.random.ranf()) # distance to travel (in mean free paths)
    if is_outside_scoring_region(pos,geom):
        new_pos = ray_trace_outside(pos, angle, geom) # in vacuum
        if is_inside_scoring_region(new_pos, geom):
            new_pos = ray_trace_inside(new_pos, angle, geom, L, st)
            if is_outside_scoring_region(new_pos, geom):
                new_pos = ray_trace_outside(new_pos, angle, geom) # in vacuum
        return new_pos

    else:
        new_pos = ray_trace_inside(pos, angle, geom, L, st)
        if is_outside_scoring_region(new_pos, geom):
            new_pos = ray_trace_outside(new_pos, angle, geom) # in vacuum
        return new_pos

def resolve_collision(old_angle, st, ss):
    r = np.random.ranf()
    if r < ss/st: #isotropic scatter
        return 2. * np.pi * np.random.ranf()
    else: #absorption
        return None





def main():
    np.random.seed(111)
    # cross sections
    st = 3.e-3
    ss = 2.5e-3
    dE_absorb = 1.
    dE_scatter = 0.1

    show_track = True
    track_limit = 100
    tracks = []

    geom = load_geometry('BL_small.png')
    dose = np.zeros_like(geom[2])

    n_particle = int(1e6)
    (init_pos1, init_angle1) = initialize_particles(int(n_particle/3+1), -400., -400., np.pi / 4. + np.pi/60, np.pi/120.)
    (init_pos2, init_angle2) = initialize_particles(int(n_particle/3+1), -400., -400., np.pi / 4. - np.pi/60, np.pi/120.)
    (init_pos3, init_angle3) = initialize_particles(int(n_particle/3+1), -400., -400., np.pi / 4., np.pi/120.)
    init_pos = init_pos1
    init_pos = np.append(init_pos, init_pos2, axis = 0)
    init_pos = np.append(init_pos, init_pos3, axis = 0)
    init_angle = init_angle1
    init_angle = np.append(init_angle, init_angle2, axis = 0)
    init_angle = np.append(init_angle, init_angle3, axis = 0)

    start_time = time.time()
    print('Progress:')

    for n in range(n_particle):
        if n > 0 and (n+1) % (n_particle/10) == 0:
            pct = int(100.*float(n+1)/float(n_particle))
            print(str(pct) +' %...', end = ' ')
            now_time = time.time()
            print('Time elapsed: ' + time_to_string_hh_mm_ss(now_time - start_time) + ' Estimated time left:', end=' ')
            time_left = float(n_particle - n)/float(n) * (now_time - start_time)
            print(time_to_string_hh_mm_ss(time_left))

        if show_track and n < track_limit:
            track_n = []
            track_n.append(init_pos[n,:])
        old_pos = init_pos[n,:]
        new_pos = init_pos[n,:]
        old_angle = init_angle[n]
        new_angle = init_angle[n]

        while is_inside_bbox(new_pos, geom) and new_pos is not None:
            if debug_print:
                print('p')
            new_pos = transport_until_next_collision(old_pos, old_angle, geom, st)
            old_pos = np.copy(new_pos)
            if show_track and n < track_limit:
                track_n.append(np.copy(new_pos))
            if is_inside_scoring_region(new_pos, geom):
                new_angle = resolve_collision(old_angle, st, ss)
                if new_angle is None:
                    dose[int(new_pos[0]), int(new_pos[1])] += dE_absorb
                    new_pos = None # to terminate the present track loop
                else:
                    dose[int(new_pos[0]), int(new_pos[1])] += dE_scatter
                old_angle = new_angle
        if show_track and n < track_limit:
            tracks.append(track_n)

    #normalize by density
    dose = dose / geom[2]

    if show_track:
        fig, ax = plt.subplots()
        ax.imshow(np.transpose(geom[2]),cmap='viridis')
        for n in range(len(tracks)):
            for i in range(len(tracks[n])-1):
                ax.plot([tracks[n][i][0], tracks[n][i+1][0]],[tracks[n][i][1], tracks[n][i+1][1]], 'r*-',linewidth=0.2, markersize=1 )
        ax.set_xlim(geom[0][0]-20., geom[0][-1]+20.)
        ax.set_ylim(geom[1][-1]+20., geom[1][0]-20.)

        fig.savefig('tracks.png')
        #fig.show()

    figd, axd = plt.subplots()
    axd.imshow(np.transpose(dose),cmap='viridis')
    axd.set_xlim(geom[0][0]-20., geom[0][-1]+20.)
    axd.set_ylim(geom[1][-1]+20., geom[1][0]-20.)

    figd.savefig('dose.png')
    np.savetxt('dose.txt',dose)
    #figd.show()


if __name__ == "__main__":
    main()
