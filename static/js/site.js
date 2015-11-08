$(function() {
  $('#leftchevbutton').on('click', function() {
    $('#content').val(function(n, c) {
      return c + '<';
    });
  });

  $('#rightchevbutton').on('click', function() {
    $('#content').val(function(n, c) {
      return c + '>\n';
    });
  });

  $('#embedbutton').on('click', function() {
    $('#content').val(function(n, c) {
      return c + '[!embed?max_width=300]()';
    });
  });
});
