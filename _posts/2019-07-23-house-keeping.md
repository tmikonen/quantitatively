---
layout: post
title: House Keeping
subtitle: Paternity Leave and Lift & Shift
#post_description: --
bigimg: /img/house_keeping/koski.jpg
tags: [Blogging, Comments, Azure]
#usemathjax: true
---

## House Keeping

*Updated on August 6, 2019.*

This time, it's a very short post. For the next several weeks, I'm on a parental leave from my day job. I'll be spending a lot more time doing, literally, house-keeping.

On the Old School Magic front, I find myself also on house-keeping duty. Instead of writing about the fun stuff I've been working on for this blog, or the awesome [Ivory Cup 4](http://www.wak-wak.se/ic4) I went to at the beginning of July, I'm, doing technical blog maintenance. Why? Simply, because the [third party service provider](http://www.just-comments.com) that I have been using to host the blog comments has decided to change their business model. While I have really liked their service for the most part, my primary reasons for using it have been 1) it's add-free and, 2) it's monetarily free (apart from the initial investment of about 5 euros). Starting from August, their service would cost me about 60 euros per year, which in my opinion is too much for this kind of a low-traffic, niche of a niche blog.

After searching for different options to provide the commenting service, I decided to host the comments myself. I got the idea and part of the implementation from the [Haacked blog](https://haacked.com/archive/2018/06/24/comments-for-jekyll-blogs/). Basically, on the static github pages one can implement an html form for submitting comments, which then accesses an Azure Function App. The app runs on the Azure cloud, receives the comments and processes them. In [their implementation](https://damieng.com/blog/2018/05/28/wordpress-to-jekyll-comments), the app creates a github pull request. I went for a slightly more old school route and settled for email forwarding. So I'll need to manually review and push the comments to the blog before they get published. But so far, with about 20 comments over the last 8 or 9 months, I think that the amount of work is doable. If not, I'll need to revise the decision at a later time.

At the moment, the system is mostly up and running. I'll still need to clean up the test comments and import the ones from the old system. But the app is online and forwarding the comments, so feel free to test it. And if you run into any problems, please drop me an email (you'll find the link at the bottom of the page).
