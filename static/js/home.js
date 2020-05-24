$(function() {
  $(".typed").typed({
    strings: [
      "stat bee.bayo<br/>" +
      "><span class='caret'>$</span> skills: automation, Software testing, continuous testing, continuous integration<br/> ^100" +
      "><span class='caret'>$</span> job: Quality Engineer at: <a href='http://www.fanduel.com/'>FanDuel Edinburgh</a><br/> ^100" +
      "><span class='caret'>$</span> hobbies: photography, travel, <a href='http://www.rish.space/blog'>writing</a><br/> ^300" +
      "><span class='caret'>$</span> alias: Bee <br/>"/*
      "><span class='caret'>$</span> <a href='/timeline'>timeline</a> <a href='http://www.github.com/adebayoadegunloyefanduel/'>github</a> <a href='https://www.linkedin.com/in/adebayo-bayo-adegunloye-9a18ba55/'>linkedin</a> <a href='https://medium.com/@beebayoadegunloye'>blog</a><br/>"*/
    ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 0.001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});
