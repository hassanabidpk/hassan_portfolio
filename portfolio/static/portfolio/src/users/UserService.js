(function(){
  'use strict';

  angular.module('users')
         .service('userService', ['$q', UserService]);

  /**
   * Users DataService
   * Uses embedded, hard-coded data model; acts asynchronously to simulate
   * remote data service call(s).
   *
   * @returns {{loadAll: Function}}
   * @constructor
   */
  function UserService($q){
    var users = [
      {
        name: 'About me',
        avatar: 'static/portfolio/assets/svg/profile_pic.svg',
        content: 'I am working as Senior software engineer (iOS application developer).I am key player of the team who developed KineMaster (video editing app). I teach Python and Android programming through a community MOOC Circle which I co-founded with colleague in Seoul. I am also a free-lance full-stack developer and loves to share code via Github.'
      },
      {
        name: 'Skills',
        avatar: 'static/portfolio/assets/svg/coding.svg',
        content: 'Java, C, Python, PHP, Javascript, Objective-C, Swift, Google Cloud Platform, Shell Scripting'
      },
      {
        name: 'Projects',
        avatar: 'static/portfolio/assets/svg/business29.svg',
        content: "NexPlayer SDK, KineMaster, Seoul Mate, Global MOOC Campus, MOOC Circle"
      },
      {
        name: 'Hacks',
        avatar: 'static/portfolio/assets/svg/laptop_mac.svg',
        content: 'Raspberry pi, Arduino, Apple Watch (Details coming soon)'
      },
      {
        name: 'Talks',
        avatar: 'static/portfolio/assets/svg/ic_video.svg',
        content: 'Udacity Study Jam Session in South Korea. From Dec 2014 to Feb 2015 Android developers in South Korea took part in a number of Udacity Study Jam sessions to learn the fundamentals of Android. Listen to +Hassan Abid tell his story at the GDG Android Korea conference about learning from our +Udacity courses and the Korean Google Developers Study Jams. Link : https://youtu.be/rmB4bUEdySk '
      },
      {
        name: 'Blog',
        avatar: 'static/portfolio/assets/svg/ic_more.svg',
        content: "<h3>Coming soon<h3>"},
    ];

    // Promise-based API
    return {
      loadAllUsers : function() {
        // Simulate async nature of real remote calls
        return $q.when(users);
      }
    };
  }

})();
