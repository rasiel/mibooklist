$(document).ready(function () {
  $("#search").click(function (e) {
    e.preventDefault();
    kword = $("#keyword").val();
    if (kword && kword != '156 available book titles ...')
      $("#search_form").submit();
    else
      alert("Please enter a Book Title to search");
  });
  $("#keyword").focus(function () {
    $(this).val('');  
  });
  $("#advanced_search_button").click(function (e) {
    e.preventDefault();
    alert("here");
    title = $("#a_title").val();
    author = $("#a_author").val();
    publisher = $("#a_publisher").val();
    school = $("#a_school").val();
    subject = $("#a_subject").val();
    edition = $("#a_edition").val();
    revision = $("#a_revision").val();
    isbn = $("#a_isbn").val();
    if (title || author || publisher || school || subject || edition || revision || isbn)
    {      
      $("#advanced_search_form").submit();
    } else {
      alert('Please enter a search term');
    }
  });
});