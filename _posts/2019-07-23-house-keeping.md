---
layout: post
title: House Keeping
#subtitle:
#post_description: --
bigimg: /img/house_keeping/koski.jpg
tags: [Blogging, Comments, Azure]
#usemathjax: true
---

## House Keeping

This time, it's a very short post. Instead of writing on the fun stuff I've been working on for this blog, or the awesome [Ivory Cup 4](http://www.wak-wak.se/ic4) I went a couple of weeks ago, I find myself forced to spend time on technical blog maintenance. Why? Simply, because the [third party service provider](http://www.just-comments.com) that I have been using to host the blog comments has decided to change their business model. While I have really liked their service for the most part, my reasons for using it have been 1) it's add-free and, 2) it's free (apart from the initial investment of about 5 euros). Starting from August, the service would cost me about 60 euros per year, which in my opinion is too much for this kind of a low-traffic, niche of a niche blog.

There are, of course, free alternatives, but they either come with adds (which I definitely do not like) or other potential problems (like what just happened with my current service provider one). So, I've decided to get rid of third parties completely, and start hosting the comments myself. It's kind of tricky with static web pages like on GitHub, but there are several solutions out there.

The one that seemed to be the least troublesome to set up I found at the [Haacked blog](https://haacked.com/archive/2018/06/24/comments-for-jekyll-blogs/). It's been [originally developed by Damien Guard](https://github.com/damieng/jekyll-blog-comments), and works basically by running a private comment receiver service on Microsoft Azure. The Azure Function App catches the comments, reformats them and sends them as a pull request to the GitHub repository that hosts the blog. Seems easy enough, so that is what I am trying now.

Until I get the system fully up and running (which I hope will be soon), there may be some weird comments on the site as I am testing it. I'll clean them up and import the ones from the old system eventually.
