# USENET_Protocol_Simulation

## Overview
USENET stands for User's Network. It is a worldwide distributed discussion system available on computers. It was developed from the general-purpose Unix-to-Unix Copy (UUCP) dial-up network architecture.

## About
Tom Truscott and Jim Ellis conceived the idea in 1979, and it was established in 1980. Users read and post messages (called articles or posts, collectively termed news) to one or more topiccategories, known as newsgroups. Usenet resembles a bulletin board system (BBS) in manyrespects and is the precursor to the Internet forums that have become widely used. Discussions are threaded, as with web forums and BBSs, though posts are stored on the server sequentially.

The basic principle of Usenet News is that local servers handle most of the functionality. Usenet News standardizes two variants of the NNTP protocols: One for communication between adjacent servers, and one for communication between a client and a server. Each server candownload as much as it wants of what is available on any of the adjacent servers. Loop control is handled both by a trace list and a list of the Message-IDs of received messages stored by each server so that the server can reject the same message coming back again. 

This procedure for the distribution of news can be compared to pouring water onto a flat horizontal surface; the water flows out in all directions. A server tells its adjacent servers which items it offers, and the server requests those it has notalready got via another route. Sometimes, there is only one way for news to be distributed between groups of servers. 

The procedure described in this figure causes wait times between an IHAVE and a SENDME command. To avoid this, an alternative procedure much used today is to instead use twocommands, CHECK and TAKETHIS. CHECK asks a server whether it wants certain articles,and TAKETHIS sends articles. The server which provides articles can use TAKETHIS to sendarticles, that it believes the receiving server wants, even if the receiving server has not asked forthis. This allows for a stream of TAKETHIS commands sending probably new articles.

Transmission is faster because the sending server can send articles that the receiving server already has. This might seem to be inefficient, but the advantage of streaming new articles ismore valuable if more than 95 % of the articles are actually new. In addition, Usenet News provides an interesting functionality that restricts communication toonly those members of a newsgroup who work in the same organization or live in the same area or country.
