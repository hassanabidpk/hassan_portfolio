(function(){

  angular
       .module('users')
       .controller('UserController', [
          'userService', '$mdSidenav', '$mdBottomSheet', '$log', '$q',
          UserController
       ]);

  /**
   * Main Controller for the Angular Material Starter App
   * @param $scope
   * @param $mdSidenav
   * @param avatarsService
   * @constructor
   */
  function UserController( userService, $mdSidenav, $mdBottomSheet, $log, $q) {
    var self = this;

    self.selected     = null;
    self.users        = [ ];
    self.selectUser   = selectUser;
    self.toggleList   = toggleUsersList;
    self.share        = share;

    // Load all registered users

    userService
          .loadAllUsers()
          .then( function( users ) {
            self.users    = [].concat(users);
            self.selected = users[0];
          });

    // *********************************
    // Internal methods
    // *********************************

    /**
     * First hide the bottomsheet IF visible, then
     * hide or Show the 'left' sideNav area
     */
    function toggleUsersList() {
      var pending = $mdBottomSheet.hide() || $q.when(true);

      pending.then(function(){
        $mdSidenav('left').toggle();
      });
    }

    /**
     * Select the current avatars
     * @param menuId
     */
    function selectUser ( user ) {
      self.selected = angular.isNumber(user) ? $scope.users[user] : user;
      self.toggleList();
    }

    /**
     * Show the bottom sheet
     */
    function share($event) {
        var user = self.selected;

        $mdBottomSheet.show({
          parent: angular.element(document.getElementById('content')),
          templateUrl: 'static/portfolio/src/users/view/contactSheet.html',
          controller: [ '$mdBottomSheet', UserSheetController],
          controllerAs: "vm",
          bindToController : true,
          targetEvent: $event
        }).then(function(clickedItem) {
          clickedItem && $log.debug( clickedItem.name + ' clicked!');
        });

        /**
         * Bottom Sheet controller for the Avatar Actions
         */
        function UserSheetController( $mdBottomSheet ) {
          this.user = user;
          this.items = [
            { name: 'Github'       , icon: 'github'       , icon_url: 'static/portfolio/assets/svg/github.svg', urlPath: "https://github.com/hassanabidpk/"},
            { name: 'Twitter'     , icon: 'twitter'     , icon_url: 'static/portfolio/assets/svg/twitter.svg', urlPath: "https://twitter.com/hassanabidpk"},
            { name: 'Google+'     , icon: 'google_plus' , icon_url: 'static/portfolio/assets/svg/google_plus.svg', urlPath: "https://plus.google.com/+HassanAbid/"},
            { name: 'Linkedin'     , icon: 'linkedin'    , icon_url: 'static/portfolio/assets/svg/linkedin.svg', urlPath: "https://kr.linkedin.com/pub/hassan-abid/12/700/66b"}
          ];
          this.performAction = function(action) {
            window.location.href = action.urlPath;
            $mdBottomSheet.hide(action);
          };
        }
    }

  }

})();
