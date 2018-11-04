# Scantry #
![Banner](https://i.imgur.com/cbcKtKC.png)
*("scan" + "pantry")*

Scantry is a mobile application that allows users to scan and categorize their food items real-time, keeping an inventory of what they have that can be accessed online.

Made for ECHacks 2018.

## Inspiration ##
We were inspired to build this app for two main factors. First, at this hackathon we were able to listen to a presentation about Machine Vision, which we found incredibly interesting. In fact, throughout the process of coming up with the idea for this project we focused on integrating and applying Clarifai's Machine Vision API in order to demonstrate the power of this concept.

Second, we love food. As an integral part of our lifestyles, we deeply recognize the importance to organize and keep track of one's own groceries. But in all seriousness, the issues of the tons (literally) of food waste created every day due to expired goods, as well as the lack of a simple and accessible way to cataloguing a personal inventory of such groceries, provided us with an opportunity to solve them and create something new.

The combination of these two factors thereby led to our idea, a simple management system taking advantage of a new technology. For us, the choice was as easy as eating another slice of cold cheese pizza.

## Description ##
Scantry is comprised of a few elements interacting with one another-to illustrate how they work, let's imagine how Scantry would work chronologically, in a situation where its user just bought some groceries. The first element is a mobile app, built with Expo.io, a React Native framework. The user uses a camera interface to scan the grocery items in front of them. The Clarifai's Machine Vision API within the app identifies the different items (like an apple, orange, or soup can) and records them down as data.

After this, data is then pushed, real-time to Google Cloud Platform's Firebase database platform. Finally, a website draws data from Firebase to display this information online, which the user can access. In this way, the user can create a catalog of what they've bought simply by scanning items with their phone, and can similarly very easily view the list of food they already have. Goodbye, shopping lists and repeated buys.

## Compilation and Usage ##
Dependencies:
* React Navigation
* Firebase Admin 2.13.0 or later

We used the following technologies:
* Implementation of Clarifai's Machine Vision API to identify and categorize items
* React Native through Expo.io
* Database hosting on Firebase
* Website deployment using Bootstrap/Netlify

Of course, in order to use the mobile app, we assume the user's phone has a camera for which they have allowed our app to access.

## Next Steps ##
We will be very direct when we state that getting the Clarifai API to work was **not** easy.  In fact, as one of the team members is writing this README another is still trying to troubleshoot the code. Therefore, while the essential functionality of our mobile app works like it should, some objects aren't properly identified all of the time, and we weren't able to focus on fine-tuning the details, such as improving the UI/UX design of our app and website. Given some more time, we would definitely like to make the user environment a little more friendly.

Other potential areas of expansion are extensions upon the idea of responsible management of groceries/food. For example, we would like to set up a function that suggests recipes users can make using the groceries listed in their database. While ambitious, we would also like to add functionality with Google Home/Amazon Alexa devices, so that users could ask for and edit their grocery lists via verbal interaction with their smart home devices. This would be possible if we added compability and synchronization with those platforms, but that's a prospect for later.

## Gallery ##
![Screenshot1](https://i.imgur.com/TXXKfOt.png)

The user interface of the mobile app. Below are buttons for picturing and classifying the objects seen in the camera view, and a button which takes the user to the list of their recorded items. 


![Screenshot2](https://i.imgur.com/xB9S7gX.jpg)

Once an image is taken, objects are classified using the Clarifai API. Here, an orange has been classified (this is a different image from water bottle in the previous picture)


![Screenshot3](https://i.imgur.com/dbSdOje.jpg)

List of the inventory the user has in the app.


![Website](https://i.imgur.com/qGnel46.png)

The Scantry website; users can find their inventory of items online as well.
