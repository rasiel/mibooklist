$(document).ready(function () {
  $("#search, #search2").click(function (e) {
    e.preventDefault();
    id = $(this).attr("id");
    alert(id);
    if (id == "#search") {
      kword = $("#keyword").val();
      search_form = "#search_form";
    } else {
      kword = $("#keyword2").val();
      search_form = "#search_form2";
    }
    
    if (kword && kword != '156 available book titles ...') {    
      $(search_form).submit();
    } else {
      alert("Please enter a Book Title to search");
    }
  });
  $("#keyword, #keyword1").focus(function () {
    $(this).val('');  
  });
  $("#advanced_search_button").click(function (e) {
    e.preventDefault();
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