$(function(){
  // // * 当鼠标放在p标签上时，颜色变为红色
  // $('p').mouseover(function(e){
  //   $(this).css('color', 'red');
  // });
  // $('p').mouseout(function(e){
  //   $(this).css('color', 'blue');
  // });
  //
  // // tr的偶数行显示#eee颜色
  // $('tr:even').css('backgroundColor', '#eee')
  //
  // // 当鼠标单击tr时，显示深色，其他tr都显示白色
  // $('tr').click(function(e){
  //   $(this).css('backgroundColor', '#aaa')
  //   $(this).siblings().css('backgroundColor', '#fff')
  // });

  console.log($('#diyige'));

  // 展示元素的content
  // 更改元素的content
  console.log($('h1').html())
  $('h1').html('Hello,kkkkkkkkkkk');

  // 给元素添加class
  $('#diyige').addClass('green');


  $(':button').click(function(e){
    e.preventDefault();
    // var submittedMsg = $(':text[name="message"]').val();
    $.ajax({
      type: 'GET',
      url: '/api/iterm/'
    })
      .done(function(responseText){
        console.log($('form').serialize())
        // console.log(responseText);
        $('p[name="test_ajax"]').html('your message is ' + responseText[0].name);
        $(':input[id="show_place"]').val('your message is ' + responseText.toString());
      })
      .fail(function(jqXHR, status, error){
        alert(jqXHR.responseText);
      })
      .always(function(){
        $('#last').after('<p> thank uuuuuuuuuu</p>');
      })
  });

  // 获取元素的text
  console.log($('p[name="Strong"]').text());

  // 获取元素的html（包含元素内部的标签)
  console.log($('p[name="Strong"]').html());

  // 给元素后添加内容
  $('p[name="Strong"]').append("!!!!!")

  // Jquery的 event处理
  $('#theForm').on('submit', function() { console.log("haha")});
  $('#theForm').submit(function() {console.log('haha')});
  // 或者
  $('#theForm').on('submit', validateForm);
  function validateForm() { console.log('haha')};

  // 其他的方法还有mouseover, mouseout ... keypress, keyup, keydown

  // .hover()方法
  $('p[name*="hover"]').hover(
    function() { // 相当于mouseover
      //$(this).show();
      $(this).css('color', "red")
    },
    function() { // 相当于mouseout
      $(this).fadeOut();
      $(this).css('color', "green")
    }
  );

  // event 的各种属性
  // target; pageX, pageY; screenX, screenY; which; shiftkey; data
  $('p[name*="event"]').click(function(event) {
    var xpos = event.pageX;
    var ypos = event.pageY;
    alert('X: ' + xpos + "; Y:" + ypos);
  });

  // 隐藏默认action，比如a标签的默认动作是让你跳转至另外一个页面
  // 使用preventDefault()可以让他不执行跳转操作
  $('a[name*="atag"]').click(function(event) {
    event.preventDefault()
    var xpos = event.pageX;
    var ypos = event.pageY;
    var target = event.target;
    alert('X: ' + xpos + "; Y:" + ypos + " Taget: " + target);
  });

  // jquery如何处理form
  // :input, :submit; text;等，注意:input会直接过滤input textarea, select, button等标签
  // form常用event
  // .submit(); .reset(); .change();, .click(); .focus(); .blur()
  // 获取input value: .val()
  // 设置inputvalue .val(values)




});
