// The following is used to support tabbing in textareas. This is also a fine example of how to interact with the
// Text area.


               $(document).delegate('#textbox', 'keydown', function(e) {



              var keyCode = e.keyCode || e.which;

              if (keyCode == 9) {
                e.preventDefault();
                var start = $(this).get(0).selectionStart;
                var end = $(this).get(0).selectionEnd;

                // set textarea value to: text before caret + tab + text after caret
                $(this).val($(this).val().substring(0, start)
                            + "\t"
                            + $(this).val().substring(end));

                // put caret at right position again
                $(this).get(0).selectionStart =
                $(this).get(0).selectionEnd = start + 1;
              }
            });
             $(document).delegate('#textbox', 'keyup', function(e) {



              var keyCode = e.keyCode || e.which;


//              So change of plans. We're handling key strokes a bit differently now.
//              Key down events are going to be stored in a stack until key-up events are registered.
            });