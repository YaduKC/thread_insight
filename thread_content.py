thread_1 = """<div id="maincontent" class="col-xs-12 col-sm-12 col-md-9 col-lg-10">




	
	


<div id="alertdiv"><div class="noticetemplate template" style="display: block;">
	<div class="alert alert-success alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
		<span id="msg">Your profile is missing a photo. <a href="/account?page=profile&amp;profilesubid=0">Add one now</a>.</span>
	</div>
</div></div>

<div class="noticetemplate template">
	<div class="alert alert-success alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
		<span id="msg"></span>
	</div>
</div>
<div class="alerttemplate template">
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
		<span id="msg"></span>
	</div>
</div>
<div class="alertnoclosetemplate template">
	<div class="alert alert-danger" role="alert">
		<span id="msg"></span>
	</div>
</div>



 
<script>
var $alerttemplate = $(".alerttemplate");
var $alertnoclosetemplate = $(".alertnoclosetemplate");
var $noticetemplate = $(".noticetemplate");
function createAlert(msg, isError, autoClose, noClose) {
	if (isError == false) {
		$newPanel = $noticetemplate.clone();
	} else {
        if (noClose) {
		  $newPanel = $alertnoclosetemplate.clone();
        } else {
		  $newPanel = $alerttemplate.clone();
        }
	}
	$newPanel.find("#msg").html(msg);
	if (autoClose == true) {
		$("#alertdiv").append($newPanel.fadeTo(2000, 500).slideUp(500, function(){
		    $newPanel.slideUp(500);
		    $newPanel.remove();
		}));  	
	} else {
		$("#alertdiv").append($newPanel.fadeIn());
	}
    return $newPanel;
}

























createAlert("Your profile is missing a photo. <a href='/account?page=profile&profilesubid=0'>Add one now</a>." , false, false, false);














































































































































































































































</script>







<script>
  // doLike toggles a like for a person.
  function doLike(groupname, numlikes, msgid, like, csrf) {
    $.ajax({
      url: groupname+"/like?msgid="+msgid+"&like="+like+"&csrf="+csrf,
      cache: false,
    });
    if (like == true) {
      numlikes++
    } else {
      numlikes--
    }
    displayLikes(groupname, numlikes, msgid, like, csrf);
    displayLikeStats(groupname, numlikes, msgid, like);
  }

  // displayLikes displays the Like/Unlike link button.
  function displayLikes(groupname, numlikes, msgid, hasliked, csrf) {
    console.log("in displayLikes")
    if (hasliked == true) {
      likedata = "<span id='likebutton"+msgid+"'><a href='#' onclick='doLike(\""+groupname+"\","+numlikes+","+msgid+", false, \""+csrf+"\");return false;'><i class=\"fa fa-thumbs-up\"></i> Unlike</a></span>"
    } else {
      likedata = "<span id='likebutton"+msgid+"'><a href='#' onclick='doLike(\""+groupname+"\","+numlikes+","+msgid+", true, \""+csrf+"\");return false;'><i class=\"fa fa-thumbs-up\"></i> Like</a></span>"
    }
    $("#likebutton"+msgid).html(likedata);
  }

  // displayLikeStats displays the line that shows how many people have liked this.
  function displayLikeStats(groupname, numlikes, msgid, hasliked) {
    if (hasliked == false && numlikes == 0) {
      $("#likestats"+msgid).html("<span id='likestats"+msgid+"'></span>");
      return
    }
    likedata = "<span id='likestats" + msgid + "'><i class='fa fa-thumbs-up'></i> "
    if (hasliked == true) {
      likedata += "You"
      if (numlikes > 1) {
        likedata = likedata + " and <a href='#' onclick='showLikes(\"" + groupname + "\"," + msgid + ");return false;'>" + (numlikes-1)
        if (numlikes == 2) {
          likedata = likedata + " other"
        } else {
          likedata = likedata + " others"
        }
      }
    } else {
        likedata += "<a href='#' onclick='showLikes(\"" + groupname + "\"," + msgid + ");return false;'>" + numlikes
        if (numlikes == 1) {
          likedata = likedata + " person"
        } else {
          likedata = likedata + " people"
        }
    }
    likedata = likedata + "</a> liked this</span>"
    $("#likestats"+msgid).html(likedata);
  }

  // showLikes fetches all the likes for a message and pops up the dialog box to show them.
  function showLikes(groupname, msgid) {
    console.log(groupname)
    $.getJSON(fixupURL(groupname+"/getlikes?msgid="+msgid), function( data ) {
        htmldata = '<table class="table the-table table-condensed table-responsive">'
        jQuery.each(data, function() {
          htmldata += '<tr><td valign="center">' + this.Icon + ' ' + this.Profile + '</td></tr>'
        });
        htmldata += '</table>'
        $("#showlikesbody").html(htmldata);
        $('#showlikesmodal').modal({show:true})
      }
    );
  }
</script>

<!-- show likes modal -->
<div class="modal fade" id="showlikesmodal" tabindex="-1" role="dialog" aria-labelledby="showlikesmodalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="showlikesmodalLabel">Likes</h4>
      </div>
      <div class="modal-body">
        <div id="showlikesbody"></div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Close</button>
      </div>
    </div>
  </div>
</div>




<script>
  /**
   * Checks if value is empty. Deep-checks arrays and objects
   * Note: modIsEmpty([]) == true, modIsEmpty({}) == true, modIsEmpty([{0:false},"",0]) == true, modIsEmpty({0:1}) == false
   * @param value
   * @returns {boolean}
   */
  function isEmpty(value) {
    var isEmptyObject = function (a) {
      if (typeof a.length === 'undefined') {
        // it's an Object, not an Array
        var hasNonempty = Object.keys(a).some(function nonEmpty(element) {
          return !isEmpty(a[element]);
        });
        return hasNonempty ? false : isEmptyObject(Object.keys(a));
      }

      return !a.some(function nonEmpty(element) {
        // check if array is really not empty as JS thinks
        return !isEmpty(element); // at least one element should be non-empty
      });
    };
    return (
      value == false ||
      typeof value === 'undefined' ||
      value == null ||
      (typeof value === 'object' && isEmptyObject(value))
    );
  }

var editor = (function () {

  // modDeletedDraft indicates the draft has been deleted, so we shouldn't try to save to it.
  var modDeletedDraft = false;
  var modDestroyedEditor = false;
  var modUnloading = false;

  // uploaderPrompt pops up either the appropriate web dialog, or the camera picker
  function modUploaderPrompt(doctype, id, draftid, groupurl, csrf) {
    console.log("UPLOADERPROMPT: V4");
    console.log("in uploaderPrompt, draftid=", draftid);
    if (typeof Capacitor !== 'undefined') {
      takePicture(doctype, id, draftid, groupurl, csrf);
      return;
    }
    if (doctype == "pictures") {
      $('#addPicturesModal' + id).modal({});
      return;
    } else if (doctype == "attachments") {
      $('#addAttachmentsModal' + id).modal({});
      return
    }
  }


  /**
   * Checks if value is empty. Deep-checks arrays and objects
   * Note: modIsEmpty([]) == true, modIsEmpty({}) == true, modIsEmpty([{0:false},"",0]) == true, modIsEmpty({0:1}) == false
   * @param value
   * @returns {boolean}
   */
  function modIsEmpty(value) {
    var isEmptyObject = function (a) {
      if (typeof a.length === 'undefined') {
        // it's an Object, not an Array
        var hasNonempty = Object.keys(a).some(function nonEmpty(element) {
          return !modIsEmpty(a[element]);
        });
        return hasNonempty ? false : isEmptyObject(Object.keys(a));
      }

      return !a.some(function nonEmpty(element) {
        // check if array is really not empty as JS thinks
        return !modIsEmpty(element); // at least one element should be non-empty
      });
    };
    return (
      value == false ||
      typeof value === 'undefined' ||
      value == null ||
      (typeof value === 'object' && isEmptyObject(value))
    );
  }

  function modDestroyAllEditors(evt) {
    console.log("In modDestroyAllEditors");
    modDestroyedEditor = true;
    while (tinymce.editors.length > 0) {
      console.log("Removing");
      tinymce.remove(tinymce.editors[0]);
    }
    if (retryTimer != null) {
      console.log("clearing retryTimer");
      clearInterval(retryTimer);
    }
    document.body.removeEventListener("gio:destroy", modDestroyAllEditors);
  }

  function modUploadData(draftid, csrf, inline) {
    let obj = {};
    obj['csrf'] = csrf;
    obj['draftid'] = draftid;
    obj['ajaxupload'] = '1';
    obj['upload'] = '1';
    if (inline == true) {
      obj['inline'] = '1';
    }
    return obj;
  }

  // attach the uploader to the correct buttons
  function modInitDeviceUploader(id, draftid, csrf, groupurl) {
  }

  // attach the uploader to the correct buttons
  function modInitWebUploader(id, draftid, csrf, groupurl) {
    if (document.documentElement.clientWidth > 767) {
      $('#attachmentupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, false),
        showClose: false,
        showUpload: false,
        previewFileType: 'any',
        uploadAsync: false,
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
      $('#pictureupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, true),
        showClose: false,
        showUpload: false,
        previewFileType: 'any',
        uploadAsync: false,
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
    } else {
      $('#attachmentupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, false),
        previewFileType: 'any',
        uploadAsync: false,
        showClose: false,
        showUpload: false,
        dropZoneTitle: 'Click folder icon to select files ...',
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
      $('#pictureupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, true),
        previewFileType: 'any',
        uploadAsync: false,
        showClose: false,
        showUpload: false,
        dropZoneTitle: 'Click folder icon to select files ...',
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
    }
    $('#attachmentupload' + id).on('filebatchuploadcomplete', function (
      event,
      files,
      extra
    ) {
      console.log('File batch upload complete');
      modUpdateAttachments(id, draftid, csrf, groupurl);
      $('#addAttachmentsModal' + id).modal('hide');
      $('#attachmentupload' + id).fileinput('clear');
    });
    $('#pictureupload' + id).on('filebatchuploadsuccess', function (
      event,
      data,
      previewId,
      index
    ) {
      let files = data.response;
      console.log('Picture file batch upload complete');
      for (var i = files.length - 1; i >= 0; i--) {
        fileurl = files[i];
        console.log('FILE: ' + files[i]);
        console.log('URL: ' + fileurl);
        imghtml = '<img src="' + fileurl + '"/>';
        console.log('imghtml: ' + imghtml);
        tinymce.activeEditor.insertContent(imghtml);
      }
      $('#addPicturesModal' + id).modal('hide');
      $('#pictureupload' + id).fileinput('clear');
    });
  }

  function modUpdateAttachments(id, draftid, csrf, groupurl) {
    // call the real function after 3 seconds to allow S3 to do whatever it needs to do to update
    // results
    setTimeout(function () { modDoUpdateAttachments(id, draftid, csrf, groupurl); }, 3000);
  }
  // modDoUpdateAttachments fetches a list of attachments and displays them on the page.
  function modDoUpdateAttachments(id, draftid, csrf, groupurl) {
    console.log('in modUpdateAttachments');
    upload = { draftid: draftid, csrf: csrf, list: '1' };
    $.ajax({
      url: fixupURL(groupurl + '/draftop'),
      cache: false,
      data: upload,
      method: 'POST',
      xhrFields: {
        withCredentials: true
      },
      dataType: 'json',
      error: function (xhr, ajaxOptions, thrownError) {
        if (modDeletedDraft == false && modDestroyedEditor == false) {
          createAlert("There was an error saving the draft. Please reload the page.", true, false)
        }
      }
    }).done(function (response) {
      // Do something with the request
      console.log('update attachments');
      // reload the page now
      if (response == null) {
        $('#attachments' + id).replaceWith(
          "<div id='attachments" + id + "'></div>"
        );
      } else {
        wrap = '<div id="attachments' + id + '">Attachments:<ul>';
        count = 0;
        for (i = 0; i < response.length; i++) {
          if (response[i].Inline == false) {
            wrap +=
              '<li>' +
              response[i].Name +
              ' (' +
              response[i].Size +
              ') <a href=\'javascript:deleteAttachment("' +
              id +
              '","' +
              draftid +
              '","' +
              csrf +
              '","' +
              groupurl +
              '","' +
              response[i].Num +
              "\")'><i class='fa fa-times'></i></a></li>";
            count++;
          }
        }
        wrap += '</ul><br /></div>';
        if (count > 0) {
          $('#attachments' + id).replaceWith(wrap);
        } else {
          $('#attachments' + id).replaceWith(
            "<div id='attachments" + id + "'></div>"
          );
        }
      }
    });
  }

  var modTimeoutId;
  function modOnFormChange(id, draftid, groupurl, csrf) {
    clearTimeout(modTimeoutId);
    if (modSaving == true) {
      modTimeoutId = setTimeout(function () {
        // Runs 1 second (1000 ms) after the last change
        modOnFormChange(id, draftid, groupurl, csrf);
      }, 1000);
      return;
    }
    modTimeoutId = setTimeout(function () {
      // Runs 1 second (1000 ms) after the last change
      modSaveDraft(id, draftid, groupurl, csrf, false);
    }, 1000);
  }

  var modSaving = false;

  // modSaveDraft saves the current form state in the draft.
  function modSaveDraft(id, draftid, groupurl, csrf, onLeave) {
    if (draftid == 0) {
      console.log("DraftID 0, not modSaving");
      return;
    }
    console.log("DELETEDDRAFT IS:", modDeletedDraft);
    console.log("DESTROYEDEDITOR IS:", modDestroyedEditor);
    if (modDeletedDraft == true) {
      console.log('NOT SAVING BECAUSE OF DELETED');
      return;
    }
    if (modDestroyedEditor == true) {
      console.log('NOT SAVING BECAUSE OF DESTROYED');
      return;
    }
    modSaving = true;
    console.log('modSaving');
    var fromval = $('#from' + id).val();
    var subject = $('#subject' + id).val();
    var body = $('#editor' + id).val();
    var bodytype = $('#bodytype' + id).val();
    var private = $('#isprivate' + id).val();
    var special = '0';
    if ($('#special').prop('checked') == true) {
      special = '1';
    }
    var bccme = '0';
    if ($('#bccme').prop('checked') == true) {
      bccme = '1';
    }
    var bccall = '0';
    if ($('#bccall').prop('checked') == true) {
      bccall = '1';
    }
    var saveval = '1';
    if (onLeave == true) {
      saveval = '2';
    }
    var hashtags = $('#hashtags').val();
    upload = {
      draftid: draftid,
      csrf: csrf,
      from: fromval,
      subject: subject,
      body: body,
      bodytype: bodytype,
      special: special,
      private: private,
      bccme: bccme,
      bccall: bccall,
      hashtags: JSON.stringify(hashtags),
      mid: id,
      save: saveval
    };
    let opts = {
      url: fixupURL(groupurl + '/draftop'),
      cache: false,
      data: upload,
      method: 'POST',
      xhrFields: {
        withCredentials: true
      },
      dataType: 'json'
    };
    if (modUnloading == false) {
      // if we are unloading we don't want to retry, because sometimes
      // that can result in a spurious error, esp on Firefox
      opts.retryCount = 5;
      opts.retryVerify = modRetryVerify;
    }
    $.ajax(opts).done(function (response) {
      // Do something with the request
      console.log('saved');
      modSaving = false;
    });
  }

  // called to see if we need to continue retrying
  function modRetryVerify() {
    if (modDeletedDraft == true || modDestroyedEditor == true) {
      return false;
    }
    return true;
  }

  // stop modSaving drafts when we do a submit
  var postVar = null;

  // Code to find and return a selected piece of HTML.
  function modGetSelection(id) {
    var flag = 0;
    var sel = document.getSelection();
    var selText = '';
    id = 'msgbody' + id;
    var forkfork = document.getElementById(id);
    if (sel.rangeCount > 0) {
      var range = sel.getRangeAt(0);
      var test = range.cloneContents();
      var clonedSelection = '';
      if (typeof test.getElementByID != 'undefined') {
        clonedSelection = range.cloneContents().getElementById(id);
      }
      if (clonedSelection) {
        selText = clonedSelection.innerHTML;
      } else {
        clonedSelection = range.cloneContents();
        var startNode = sel.getRangeAt(0).startContainer.parentNode;
        //console.log(modIsChild(startNode, forkfork));
        if (modIsChild(startNode, forkfork)) {
          var div = document.createElement('div');
          div.appendChild(clonedSelection);
          selText = div.innerHTML;
        }
      }
    }

    return selText.toString();
  }
  function modIsChild(child, parent) {
    if (child === parent) return true;
    var current = child;
    while (current) {
      if (current === parent) return true;
      current = current.parentNode;
    }
    return false;
  }


  return {

    InitEditor: function (
      id,
      editorType,
      draftid,
      groupurl,
      csrf,
      handleAttachments,
      noFontChanges,
      isReply,
      isWiki,
      sig,
      onInitFunc
    ) {
      if (typeof onInitFunc === 'undefined') { onInitFunc = null; }

      //document.getElementById("editor" + id).addEventListener("gio:destroy", modDestroyAllEditors);
      document.body.addEventListener("gio:destroy", modDestroyAllEditors);
      modDeletedDraft = false;
      modDestroyedEditor = false;
      modUnloading = false;

      $('#preview' + id).hide();
      $('#addattachments' + id).hide();
      $('#return' + id).hide();
      $('#markdownlink' + id).hide();
      if (editorType == 'html') {
        if (sig != '') {
          $('#editor' + id).val(sig);
          //tinyMCE.get('editor'+id).setContent(sig);
        }
        editor.initHTMLEditor(
          id,
          draftid,
          groupurl,
          csrf,
          handleAttachments,
          noFontChanges,
          isReply,
          isWiki,
          sig,
          onInitFunc
        );
      } else {
        if (sig != '') {
          $('#editor' + id).val(sig);
        }
        editor.initPlainEditor(id, editorType);
      }
    },

    initHTMLEditor: function (
      id,
      draftid,
      groupurl,
      csrf,
      handleAttachments,
      noFontChanges,
      isReply,
      isWiki,
      sig,
      onInitFunc
    ) {

      if (typeof onInitFunc === 'undefined') { onInitFunc = null; }
      // extras: print, emoticons, image, insert, media, print
      /* All plugins:
              'advlist autolink lists link image print preview hr anchor pagebreak',
          'searchreplace wordcount visualblocks visualchars code fullscreen',
          'insertdatetime media nonbreaking save table contextmenu directionality',
          'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc'
      */
      modDeletedDraft = false;
      modDestroyedEditor = false;
      modUnloading = false;
      let attachments = '';
      if (handleAttachments == 0 || handleAttachments == 3) {
        attachments = ' addPictures addAttachments';
      }
      let fontchanges = '';
      if (noFontChanges == false) {
        fontchanges = ' fontselect fontsizeselect forecolor backcolor';
      }
      let fontawesome = ' charmap';
      let forceRootBlock = false;
      if (isWiki == true) {
        attachments += ' addWikiImage addWikiLink addWikiTOC';
        fontawesome = ' fontawesome';
        // BORK
        fontawesome = '';
        forceRootBlock = 'p';
      }
      let toolbar1 =
        'styleselect bold italic bullist numlist link blockquote alignleft aligncenter alignright' +
        attachments +
        ' advancedToolbar';
      let toolbar2 =
        'strikethrough underline hr alignjustify' +
        fontchanges +
        ' removeformat' +
        fontawesome +
        ' outdent indent undo redo preview code';

      let small_toolbar1 =
        'bold italic link blockquote' + attachments + ' advancedToolbar';
      let small_toolbar2 =
        'strikethrough underline hr alignjustify removeformat outdent indent';

      let tm_fonts =
        'Arial=arial,helvetica,sans-serif;' +
        'Arial Black=arial black,avant garde;' +
        'Comic Sans MS=comic sans ms;' +
        'Courier Neue=courier_newregular,courier;' +
        'Helvetica Neue=helvetica neue;' +
        'Helvetica=helvetica;' +
        'Impact=impactregular,chicago;' +
        'Lucida Grande=lucida grande;' +
        'Tahoma=tahoma,arial,helvetica,sans-serif;' +
        'Times New Roman=times new roman,times;' +
        'Verdana=verdana,geneva';
      let plugins = [
        'SplitBlockquote',
        'advlist autolink lists link image preview hr anchor',
        'code fullscreen',
        'nonbreaking table charmap',
        'textcolor colorpicker imagetools noneditable'
      ];
      let css =
        fixupURL('/bootstrap/3.3.6/css/bootstrap.min.css') + ',' + fixupURL('/bootstrap/3.3.6/css/bootstrap-theme.min.css') + ',' + fixupURL('/css/groupsio.css') + ',' + fixupURL('/css/tinymce.css') + ',' + fixupURL('/fontawesome/5.9.0/css/all.min.css');

      let fontsizes = '8pt 10pt 11pt 12pt 14pt 18pt 24pt 36pt';

      let codesample_languages = [
        { text: 'C', value: 'c' },
        { text: 'C#', value: 'csharp' },
        { text: 'C++', value: 'cpp' },
        { text: 'CSS', value: 'css' },
        { text: 'Go', value: 'go' },
        { text: 'HTML/XML', value: 'markup' },
        { text: 'Java', value: 'java' },
        { text: 'JavaScript', value: 'javascript' },
        { text: 'PHP', value: 'php' },
        { text: 'Python', value: 'python' },
        { text: 'Ruby', value: 'ruby' }
      ];

      let style_formats = [
        { title: 'Paragraph', block: 'p' },
        { title: 'Header 1', block: 'h1' },
        { title: 'Header 2', block: 'h2' },
        { title: 'Header 3', block: 'h3' },
        { title: 'Header 4', block: 'h4' },
        { title: 'Header 5', block: 'h5' },
        { title: 'Header 6', block: 'h6' }
      ];

      if (isReply == true) {
        toolbar1 = 'quoteMessage ' + toolbar1;
        small_toolbar1 = 'quoteMessage ' + small_toolbar1;
      }
      if (document.documentElement.clientWidth > 1000) {
        tinymce.init({
          noneditable_noneditable_class: 'fa',
          extended_valid_elements: 'span[*]',
          branding: false,
          link_context_toolbar: true,
          default_link_target: '_blank',
          link_assume_external_targets: true,
          elementpath: false,
          forced_root_block: forceRootBlock,
          content_css: css,
          relative_urls: false,
          remove_script_host: false,
          menubar: false,
          statusbar: true,
          plugins: plugins,
          toolbar1: toolbar1,
          toolbar2: toolbar2,
          font_formats: tm_fonts,
          browser_spellcheck: true,
          contextmenu: false,
          selector: '#editor' + id,
          resize: true,
          fontsize_formats: fontsizes,
          style_formats: style_formats,
          setup: function (teditor) {
              teditor.on('Init', function (e) {
              if (sig != "") {
                teditor.setContent(sig);
              } else {
                setContent(teditor);
              }
              });
            if (onInitFunc != null) {
              teditor.on('Init', function (e) {
                onInitFunc(e);
              });
            }
            teditor.on('BeforeRenderUI', function (e) {
              teditor.theme.panel
                .find('toolbar')
                .slice(1)
                .hide();
            });
            teditor.addButton('advancedToolbar', {
              tooltip: 'Show advanced toolbar',
              icon: 'fa fa-bars',
              onclick: function () {
                if (!this.active()) {
                  this.active(true);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .show();
                } else {
                  this.active(false);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .hide();
                }
              }
            });
            teditor.addButton('addPictures', {
              tooltip: 'Add pictures',
              icon: 'fa fa-image',
              onclick: function () {
                modUploaderPrompt("pictures", id, draftid, groupurl, csrf);
              }
            });
            teditor.addButton('addAttachments', {
              tooltip: 'Add attachments',
              icon: 'fa fa-paperclip',
              onclick: function () {
                modUploaderPrompt("attachments", id, draftid, groupurl, csrf);
              }
            });
            if (groupurl != '') {
              teditor.addButton('quoteMessage', {
                tooltip: 'Quote post',
                icon: 'fa fa-comment',
                onclick: function () {
                  editor.ShowMessageHistory(id, groupurl, 'html', '', sig, false);
                }
              });
            }
            if (draftid != '' && draftid != '0' && draftid != 0) {
              teditor.on('NodeChange', function () {
                //tinymce.triggerSave();
                if (tinymce.activeEditor != null) {
                  let markupStr = tinymce.activeEditor.getContent();
                  $('#editor' + id).val(markupStr);
                  modOnFormChange(id, draftid, groupurl, csrf);
                }
              });
              teditor.on('keyup', function () {
                //tinymce.triggerSave();
                let markupStr = tinymce.activeEditor.getContent();
                $('#editor' + id).val(markupStr);
                modOnFormChange(id, draftid, groupurl, csrf);
              });
            }
            if (isWiki == true) {
              // special wiki buttons
              teditor.addButton('addWikiImage', {
                tooltip: 'Insert image',
                icon: 'fa fa-image',
                onclick: function () {
                  $('#ImageModal').modal({});
                }
              });
              teditor.addButton('addWikiLink', {
                tooltip: 'Insert link to wiki page',
                icon: 'fa fa-book',
                onclick: function () {
                  $('#LinkModal').modal({});
                }
              });
              teditor.addButton('addWikiTOC', {
                tooltip: 'Insert table of contents',
                icon: 'fa fa-list-alt',
                onclick: function () {
                  $('#TOCModal').modal({});
                }
              });
            }
          }
        });
      } else {
        tinymce.init({
          branding: false,
          link_context_toolbar: true,
          default_link_target: '_blank',
          link_assume_external_targets: true,
          elementpath: false,
          forced_root_block: forceRootBlock,
          content_css: css,
          relative_urls: false,
          remove_script_host: false,
          menubar: false,
          statusbar: true,
          plugins: plugins,
          toolbar1: small_toolbar1,
          toolbar2: small_toolbar2,
          font_formats: tm_fonts,
          browser_spellcheck: true,
          contextmenu: false,
          selector: '#editor' + id,
          resize: true,
          fontsize_formats: fontsizes,
          style_formats: style_formats,
          setup: function (teditor) {
              teditor.on('Init', function (e) {
              if (sig != "") {
                teditor.setContent(sig);
              } else {
                setContent(teditor);
              }
              });
            if (onInitFunc != null) {
              teditor.on('Init', function (e) {
                onInitFunc(e);
              });
            }
            teditor.on('BeforeRenderUI', function (e) {
              teditor.theme.panel
                .find('toolbar')
                .slice(1)
                .hide();
            });
            teditor.addButton('advancedToolbar', {
              tooltip: 'Show advanced toolbar',
              icon: 'fa fa-bars',
              onclick: function () {
                if (!this.active()) {
                  this.active(true);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .show();
                } else {
                  this.active(false);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .hide();
                }
              }
            });
            teditor.addButton('addPictures', {
              tooltip: 'Add pictures',
              icon: 'fa fa-image',
              onclick: function () {
                modUploaderPrompt("pictures", id, draftid, groupurl, csrf);
              }
            });
            teditor.addButton('addAttachments', {
              tooltip: 'Add attachments',
              icon: 'fa fa-paperclip',
              onclick: function () {
                modUploaderPrompt("attachments", id, draftid, groupurl, csrf);
              }
            });
            if (groupurl != '') {
              teditor.addButton('quoteMessage', {
                tooltip: 'Quote post',
                icon: 'fa fa-comment',
                onclick: function () {
                  editor.ShowMessageHistory(id, groupurl, 'html', '', sig, false);
                }
              });
            }
            if (draftid != '' && draftid != '0' && draftid != 0) {
              teditor.on('NodeChange', function () {
                if (tinymce.activeEditor != null) {
                  //tinymce.triggerSave();
                  let markupStr = tinymce.activeEditor.getContent();
                  $('#editor' + id).val(markupStr);
                  modOnFormChange(id, draftid, groupurl, csrf);
                }
              });
              teditor.on('keyup', function () {
                //tinymce.triggerSave();
                let markupStr = tinymce.activeEditor.getContent();
                $('#editor' + id).val(markupStr);
                modOnFormChange(id, draftid, groupurl, csrf);
              });
            }
            // special wiki buttons
            teditor.addButton('addWikiImage', {
              tooltip: 'Add Image',
              icon: 'fa fa-image',
              onclick: function () {
                $('#ImageModal').modal({});
              }
            });
            teditor.addButton('addWikiLink', {
              tooltip: 'Add Link',
              icon: 'fa fa-book',
              onclick: function () {
                $('#LinkModal').modal({});
              }
            });
            teditor.addButton('addWikiTOC', {
              tooltip: 'Table of Contents',
              icon: 'fa fa-list-alt',
              onclick: function () {
                $('#TOCModal').modal({});
              }
            });
          }
        });

        // disable tooltips because they require double taps on mobile
        $('.note-editor *').tooltip('disable');
      }
    },

    initPlainEditor: function (id, editorType, handleAttachments) {
      $('#addattachments').show();
      if (editorType == 'plain') {
        $('#bodytype' + id).val('plain');
        $('#preview' + id).hide();
        $('#return' + id).hide();
        $('#preview' + id).hide();
        $('#markdownlink' + id).hide();
      } else {
        $('#bodytype' + id).val('markdown');
        $('#markdownbuttons' + id).show();
        $('#preview' + id).show();
        $('#return' + id).hide();
        $('#previewWindow' + id).hide();
        $('#markdownlink' + id).show();
      }
    },

    InitPostDraft: function (id, draftid, csrf, groupurl) {
      // save the draft when leaving the page.
      $(window).on('beforeunload', function () {
        modUnloading = true;
        modSaveDraft(id, draftid, groupurl, csrf, true);
      });

      // save the draft 1 second after a change
      $('form input, form textarea').on('input propertychange change', function () {
        modOnFormChange(id, draftid, groupurl, csrf);
      });
      modUpdateAttachments(id, draftid, csrf, groupurl);

      if (typeof Capacitor !== 'undefined') {
        modInitDeviceUploader(id, draftid, csrf, groupurl);
      } else {
        modInitWebUploader(id, draftid, csrf, groupurl);
      }
    },

    // InitReplyDraft creates a new draft, assumes a hidden form input called #draftidmid, and then calls initWindow().
    InitReplyDraft: function (
      id,
      bodytype,
      draftid,
      groupurl,
      csrf,
      handleAttachments,
      noFontChanges,
      sig
    ) {
      console.log('in InitReplyDraft draftid=' + draftid);
      modDeletedDraft = false;
      modDestroyedEditor = false;
      modUnloading = false;

      if (draftid == 0) {
        // create a new draft
        console.log('generating new draft' + groupurl);
        console.log('id=' + id);
        upload = { mid: id, csrf: csrf, body: sig };
        $.ajax({
          url: fixupURL(groupurl + '/reply'),
          cache: false,
          method: 'POST',
          data: upload,
          xhrFields: {
            withCredentials: true
          },
          dataType: 'json',
          error: function (xhr, ajaxOptions, thrownError) {
            if (modDeletedDraft == false && modDestroyedEditor == false) {
              createAlert("There was an error saving the draft. Please reload the page.", true, false)
            }
          }
        }).done(function (response) {
          console.log('reply draft created');
          console.log('draftid:' + response.DraftID);
          draftid = response.DraftID;
          toquote = modGetSelection(id);
          if (toquote != '') {
            console.log('id=' + id);
            editor.ShowMessageHistory(id, groupurl, bodytype, toquote, sig, true);
          }
          $('#draftid' + id).val(response.DraftID);
          editor.InitEditor(
            id,
            bodytype,
            draftid,
            groupurl,
            csrf,
            handleAttachments,
            noFontChanges,
            true,
            false,
            sig
          );
          editor.InitPostDraft(id, draftid, csrf, groupurl);
          console.log('id=' + id);
          $('#bodytype' + id).val(bodytype);
          $('#cancel-' + id).attr(
            'onclick',
            'editor.discardReplyDraft("' +
            id +
            '", "' +
            draftid +
            '","' +
            bodytype +
            '","' +
            csrf +
            '","' +
            groupurl +
            '");'
          );
          return;
        });
        return;
      }
      editor.InitEditor(
        id,
        bodytype,
        draftid,
        groupurl,
        csrf,
        handleAttachments,
        noFontChanges,
        true,
        false,
        sig
      );
      editor.InitPostDraft(id, draftid, csrf, groupurl);
      $('#bodytype' + id).val(bodytype);
      $('#cancel-' + id).attr(
        'onclick',
        'editor.discardReplyDraft("' +
        id +
        '", "' +
        draftid +
        '","' +
        bodytype +
        '","' +
        csrf +
        '","' +
        groupurl +
        '");'
      );
      console.log('DONE');
    },

    // discardReplyDraft deletes the draft and any attachments and returns the user to the previous page.
    discardReplyDraft: function (id, draftid, bodytype, csrf, groupurl) {
      console.log('editor delete reply draft');
      upload = { draftid: draftid, csrf: csrf, jsondelete: '1' };
      $.ajax({
        url: fixupURL(groupurl + '/draftop'),
        cache: false,
        data: upload,
        method: 'POST',
        xhrFields: {
          withCredentials: true
        },
        dataType: 'json'
      }).done(function (response) {
        // Do something with the request
        console.log("success delete reply draft");
        $('#draftid' + id).val('');
        if (bodytype == 'html') {
          tinymce.get('editor' + id).remove();
        }
        $('#subject' + id).val($('#origsubject' + id).val());
        $('#editor' + id).val('');
        modDeletedDraft = true;
        modDestroyedEditor = true;
      });
    },

    PreviewMarkdown: function (id, groupurl) {
      let markdown = $('#editor' + id).val();
      upload = { md: markdown };
      $.ajax({
        url: fixupURL(groupurl + '/previewmd'),
        cache: false,
        data: upload,
        method: 'POST',
        xhrFields: {
          withCredentials: true
        },
        dataType: 'json'
      }).done(function (response) {
        // Do something with the request
        console.log(response.markdown);
        wrap =
          '<div id="previewWindow' +
          id +
          '"><div class="well well-sm">' +
          response.markdown +
          '</div></div>';
        $('#editwindow' + id).hide();
        $('#previewWindow' + id).replaceWith(wrap);
        $('#previewWindow' + id).show();
      });

      $('#preview' + id).hide();
      $('#return' + id).show();
    },

    ReturnMarkdown: function (id) {
      $('#preview' + id).show();
      $('#return' + id).hide();
      $('#previewWindow' + id).hide();
      $('#editwindow' + id).show();
    },

    // groupReplyto is groupsio.ReplyTo
    // toggle=0 is group
    // toggle=1 is sender
    // toggle=2 is mods
    TogglePrivate: function (id, groupReplyto, toggle) {
      console.log("in TogglePrivate");
      if (groupReplyto == 2) {
        // Reply To Moderators
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').removeClass('btn-info').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 2);return false;");
          $('#grouptoggle' + id).removeClass('btn-success').addClass('btn-default');
          $('#grouptoggle' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else if (toggle == 2) {
          $('#replytype' + id).val('mods');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Mods</a>');
          $('#replybutton' + id).removeClass('btn-success').removeClass('btn-primary').addClass('btn-info');
          $('#grouptoggle' + id).removeClass('btn-success').addClass('btn-default');
          $('#grouptoggle' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group');
          $('#replybutton' + id).removeClass('btn-primary').removeClass('btn-info').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 2);return false;");
          $('#grouptoggle' + id).removeClass('btn-default').addClass('btn-success');
          $('#grouptoggle' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 2);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else if (groupReplyto == 1) {
        // Reply To Sender
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-success').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-default').addClass('btn-success');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else if (groupReplyto == 3) {
        // Reply To Group And Sender
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group & Sender');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else if (groupReplyto == 5) {
        // Reply To Followers Only
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Topic Followers Only');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else {
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      }
    },

    ClearTimeout: function() {
      clearTimeout(modTimeoutId);
    },

    ShowMessageHistory: function(
      id,
      groupurl,
      bodytype,
      selectedText,
      sig,
      firstTime
    ) {
      console.log('URL ' + groupurl);
      console.log('ID ' + id);
      if (bodytype == 'html' && firstTime == false) {
        existingmsg = tinyMCE.get('editor' + id).getContent();
      } else {
        existingmsg = $('#editor' + id).val();
      }
      if (selectedText == '') {
        upload = { preview: bodytype, id: id };
      } else {
        upload = { preview: bodytype, id: id, text: selectedText };
        if (firstTime == true) {
          existingmsg = sig;
        }
      }
      $.ajax({
        url: fixupURL(groupurl + '/previewmd'),
        cache: false,
        data: upload,
        method: 'POST',
        xhrFields: {
          withCredentials: true
        },
        dataType: 'json'
      }).done(function (response) {
        $('#editor' + id).val(response.reply + existingmsg);
        if (bodytype == 'html') {
          console.log('SETTING ' + response.reply + existingmsg);
          tinyMCE.get('editor' + id).setContent(response.reply + existingmsg);
          console.log('DONE');
        }
      });
      $('#editor' + id).focus();
    }




    /*
    $('form').submit(function(e) {
      clearTimeout(modTimeoutId);
      if (postVar != null) {
        postVar.abort();
      }
      console.log("SETTING DELETED TO TRUE");
      console.log("EVENT:", e);
      modDeletedDraft = true;
      if ($(this).hasClass('form-submitted')) {
        e.preventDefault();
        return;
      }
      $(this).addClass('form-submitted');
    });
    */
  };
}());
</script>


<form class="form-inline pull-right hidden-xs" method="get" action="https://ctolunches.groups.io/g/worldwide/search">
  <input type="hidden" name="p" value="Created,,,20,1,0,0">
  <div class="input-group">
    <input type="text" class="form-control" placeholder="Search" title="Search" name="q" size="20" value="">
    <div class="input-group-btn">
      <button class="btn btn-primary" type="submit">
        <span class="fa fa-search"></span>
      </button>
    </div>
  </div>
</form>


<span class="hidden-sm hidden-md hidden-lg pull-right" style="padding:8px 15px;"><a data-toggle="modal" data-target="#searchModal"><i class="fa fa-search"></i></a></span>
<ol class="breadcrumb">
  <li class="hidden-xs"><a href="https://ctolunches.groups.io/g/worldwide"><i class="fa fa-home"></i> worldwide@ctolunches.groups.io</a></li>
  <li><a href="https://ctolunches.groups.io/g/worldwide/topics?p=,,,0,0,0,0"><i class="fa fa-inbox"></i> Topics</a></li>
	
	<li class="active"><i class="fa fa-comments"></i> re-builds</li>
</ol>


<div class="modal fade" id="searchModal" tabindex="-1" role="dialog" aria-labelledby="searchModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="searchModalLabel">Search</h4>
      </div>
      <form class="form-horizontal" method="get" action="https://ctolunches.groups.io/g/worldwide/search">
        <div class="modal-body">
            <div class="form-group">
              <div class="col-sm-12">
                <input type="text" class="form-control" placeholder="Search" title="Search" name="q" value="">
              </div>
            </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary btn-sm"><i class="fa fa-search"></i> Search</button>
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        </div>
      </form>
    </div>
  </div>
</div>



  <div class="form-group">
  


  
    <a class="btn btn-info btn-sm bottom10" href="https://ctolunches.groups.io/g/worldwide/ft/90710568?csrf=5276883099450123193&amp;mute=1&amp;p=Created%2C%2C%2C20%2C1%2C0%2C0"><i class="far fa-volume-mute"></i> Mute This Topic</a>
  

  </div>


<div class="pull-right">
  <span class="hidden-xs" style="float:left; margin-top:8px;">
    
      <a href="https://ctolunches.groups.io/g/worldwide/topic/90710568?p=Created%2C%2C%2C20%2C2%2C0%2C0">Date <i class="fa fa-sort-up"></i></a>
    
    &nbsp;&nbsp;
  </span>
  <span class="hidden-sm hidden-md hidden-lg">
    
      <a href="https://ctolunches.groups.io/g/worldwide/topic/90710568?p=Created%2C%2C%2C20%2C2%2C0%2C0">Date <i class="fa fa-sort-up"></i></a>
    
  </span>

  
	
		<span class="hidden-xs">
			<span style="float:left; margin-top:8px;">
				
					1 - 20 of 34
				
			</span>&nbsp;
			<ul class="pagination" style="margin: 0px !important;">
				
					<li class="disabled"><a href="#"><i class="fa fa-chevron-left"><span class="sr-only">previous page</span></i></a></li>
				
				
        <li><a href="https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p=Created%2C%2C%2C20%2C1%2C20%2C0&amp;next=1"><i class="fa fa-chevron-right"><span class="sr-only">next page</span></i></a></li>
				
			</ul>
		</span>
	


</div>

  <h4>
    
    
    
    re-builds
    
    
  </h4>


<table id="records" class="table table-condensed table-striped table-fixed">
  <tbody><tr></tr>

    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5158"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Dan Richards
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 8:27am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5158"><span class="hidden-xs">#5158&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204192478">
        <div class="forcebreak" dir="auto"><meta http-equiv="content-type">
  
  
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre class="moz-signature">-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a class="moz-txt-link-abbreviated" href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>
t: @rodandar</pre>
  
</div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204192478" aria-expanded="false" aria-controls="window-204192478"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204192478"><span id="likebutton204192478"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204192478, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204192478" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204192478">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4460907"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204192478"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204192478"><span id="likestats204192478"></span></div>
        </div>
      </div>
      
        <div id="window-204192478" class="collapse">
          <form class="form" id="form204192478" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204192478" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204192478">
            <input type="hidden" id="groupname204192478" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204192478" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204192478" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204192478" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204192478">
    <textarea id="editor204192478" name="editor204192478" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204192478"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204192478"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204192478" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204192478" value="html">
              

              <div id="bccme204192478" class="checkbox">
                <label for="bccme204192478">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204192478" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204192478"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204192478" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204192478" name="preview" onclick="editor.PreviewMarkdown(204192478,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204192478" name="return" onclick="editor.ReturnMarkdown(204192478)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204192478" data-toggle="collapse" data-target="#window-204192478"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204192478" onclick="editor.TogglePrivate('204192478', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204192478" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204192478">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204192478">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204192478" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204192478&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204192478" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204192478">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204192478">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204192478" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204192478&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204192478').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204192478').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204192478", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204192478').tooltip()
            $('#showHistory204192478').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204192478, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204192478, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5159"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Sean Goodpasture
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 8:53am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5159"><span class="hidden-xs">#5159&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204194078">
        <div class="forcebreak" dir="auto"><div dir="ltr">A bit tongue in cheek, but I agree with your instincts...<div><br></div><div>10 years to build - 10 years to rebuild</div><div><br></div><div>I would pick a more modern stack and language (and go far more cloud native).&nbsp; There's too many options here, but I would pick something more accessible like nodejs or java as it will lower the TCO.</div><div><br></div><div>PHP/Laravel?&nbsp; No, never.&nbsp; Certainly not in 2022.</div><div><br></div><div>Having done this the wrong way a bunch, the most successful pattern (which as you point out is still fraught with risks) I've used &amp; seen is the strangler pattern (<a href="https://www.castsoftware.com/blog/how-to-use-strangler-pattern-for-microservices-modernization" rel="nofollow noopener" target="_blank">https://www.castsoftware.com/blog/how-to-use-strangler-pattern-for-microservices-modernization</a>).&nbsp; It takes even longer to do it this way, but it changes the risk profile completely.</div><div><br></div><div>Sean</div><div><br></div><div><br></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204194078" role="button" data-toggle="collapse" href="#quoted-204194078" aria-expanded="false" aria-controls="quoted-204194078"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204194078" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 9:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">
  

    
  
  <div>
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div>



  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204194078').on('show.bs.collapse', function () {
              $('#qlabel-204194078').text("Hide quoted text");
            })
            $('#quoted-204194078').on('hide.bs.collapse', function () {
              $('#qlabel-204194078').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204194078" aria-expanded="false" aria-controls="window-204194078"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204194078"><span id="likebutton204194078"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204194078, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204194078" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204194078">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4125372"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204194078"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204194078"><span id="likestats204194078"></span></div>
        </div>
      </div>
      
        <div id="window-204194078" class="collapse">
          <form class="form" id="form204194078" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204194078" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204194078">
            <input type="hidden" id="groupname204194078" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204194078" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204194078" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204194078" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204194078">
    <textarea id="editor204194078" name="editor204194078" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204194078"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204194078"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204194078" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204194078" value="html">
              

              <div id="bccme204194078" class="checkbox">
                <label for="bccme204194078">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204194078" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204194078"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204194078" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204194078" name="preview" onclick="editor.PreviewMarkdown(204194078,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204194078" name="return" onclick="editor.ReturnMarkdown(204194078)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204194078" data-toggle="collapse" data-target="#window-204194078"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204194078" onclick="editor.TogglePrivate('204194078', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204194078" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204194078">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204194078">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204194078" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204194078&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204194078" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204194078">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204194078">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204194078" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204194078&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204194078').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204194078').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204194078", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204194078').tooltip()
            $('#showHistory204194078').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204194078, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204194078, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5160"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    kkmiller
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 8:55am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5160"><span class="hidden-xs">#5160&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204194166">
        <div class="forcebreak" dir="auto"><div dir="ltr">Dan,<div><br></div><div>I've seen it done well maybe twice? But with a lot more failures (including a CTO telling me he could re-build the entire 15 year old codebase in .NET in three weeks—he did not succeed).</div><div><br></div><div>If I were in your shoes and starting over I'd definitely a choose a more modern language. I suspect you're right about PHP being difficult to recruit for now, but definitely&nbsp;in the future as well. If they're selling the product can you start with&nbsp;a rebuild MVP and then iterate? Maybe a smaller version at a smaller price so there are some business incentives that are realized before the whole thing is "done"?</div><div><br></div><div>I think you're right that running out of momentum/money before it's done is probably the biggest risk.</div><div><br></div><div>A few options I'd see:</div><div><br></div><div>1) Rebuild parts of it—maybe in a different language, maybe not. But start to update.</div><div>2) hire an outside firm to do a rebuild (all kinds of dragons there, but at least you don't get distracted internally? Maybe?)</div><div>3) Spend the next year culling cruft AND THEN re-consider a re-write. My guess is part of the impetus for a rewrite is a desire to just do better...a nd fixing in place will probably be easier than starting over from scratch.</div></div><br></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204194166" role="button" data-toggle="collapse" href="#quoted-204194166" aria-expanded="false" aria-controls="quoted-204194166"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204194166" class="collapse forcebreak">
            <div dir="auto"><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 9:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">
  

    
  
  <div>
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div>



  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204194166').on('show.bs.collapse', function () {
              $('#qlabel-204194166').text("Hide quoted text");
            })
            $('#quoted-204194166').on('hide.bs.collapse', function () {
              $('#qlabel-204194166').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204194166" aria-expanded="false" aria-controls="window-204194166"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204194166"><span id="likebutton204194166"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204194166, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204194166" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204194166">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388229"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204194166"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204194166"><span id="likestats204194166"></span></div>
        </div>
      </div>
      
        <div id="window-204194166" class="collapse">
          <form class="form" id="form204194166" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204194166" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204194166">
            <input type="hidden" id="groupname204194166" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204194166" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204194166" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204194166" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204194166">
    <textarea id="editor204194166" name="editor204194166" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204194166"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204194166"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204194166" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204194166" value="html">
              

              <div id="bccme204194166" class="checkbox">
                <label for="bccme204194166">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204194166" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204194166"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204194166" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204194166" name="preview" onclick="editor.PreviewMarkdown(204194166,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204194166" name="return" onclick="editor.ReturnMarkdown(204194166)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204194166" data-toggle="collapse" data-target="#window-204194166"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204194166" onclick="editor.TogglePrivate('204194166', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204194166" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204194166">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204194166">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204194166" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204194166&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204194166" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204194166">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204194166">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204194166" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204194166&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204194166').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204194166').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204194166", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204194166').tooltip()
            $('#showHistory204194166').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204194166, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204194166, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5161"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    kkmiller
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 8:56am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5161"><span class="hidden-xs">#5161&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204194201">
        <div class="forcebreak" dir="auto"><div dir="ltr">Hit send. Read Sean's words. Came back to say.... what Sean said.</div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204194201" role="button" data-toggle="collapse" href="#quoted-204194201" aria-expanded="false" aria-controls="quoted-204194201"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204194201" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 9:53 AM Sean Goodpasture &lt;<a href="mailto:goofygrin@gmail.com" rel="nofollow noopener" target="_blank">goofygrin@gmail.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div dir="ltr">A bit tongue in cheek, but I agree with your instincts...<div><br></div><div>10 years to build - 10 years to rebuild</div><div><br></div><div>I would pick a more modern stack and language (and go far more cloud native).&nbsp; There's too many options here, but I would pick something more accessible like nodejs or java as it will lower the TCO.</div><div><br></div><div>PHP/Laravel?&nbsp; No, never.&nbsp; Certainly not in 2022.</div><div><br></div><div>Having done this the wrong way a bunch, the most successful pattern (which as you point out is still fraught with risks) I've used &amp; seen is the strangler pattern (<a href="https://www.castsoftware.com/blog/how-to-use-strangler-pattern-for-microservices-modernization" target="_blank" rel="nofollow noopener">https://www.castsoftware.com/blog/how-to-use-strangler-pattern-for-microservices-modernization</a>).&nbsp; It takes even longer to do it this way, but it changes the risk profile completely.</div><div><br></div><div>Sean</div><div><br></div><div><br></div></div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 9:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">
  

    
  
  <div>
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div>



  

<p></p><p></p></blockquote></div>


  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204194201').on('show.bs.collapse', function () {
              $('#qlabel-204194201').text("Hide quoted text");
            })
            $('#quoted-204194201').on('hide.bs.collapse', function () {
              $('#qlabel-204194201').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204194201" aria-expanded="false" aria-controls="window-204194201"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204194201"><span id="likebutton204194201"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204194201, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204194201" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204194201">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388229"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204194201"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204194201"><span id="likestats204194201"></span></div>
        </div>
      </div>
      
        <div id="window-204194201" class="collapse">
          <form class="form" id="form204194201" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204194201" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204194201">
            <input type="hidden" id="groupname204194201" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204194201" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204194201" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204194201" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204194201">
    <textarea id="editor204194201" name="editor204194201" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204194201"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204194201"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204194201" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204194201" value="html">
              

              <div id="bccme204194201" class="checkbox">
                <label for="bccme204194201">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204194201" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204194201"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204194201" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204194201" name="preview" onclick="editor.PreviewMarkdown(204194201,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204194201" name="return" onclick="editor.ReturnMarkdown(204194201)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204194201" data-toggle="collapse" data-target="#window-204194201"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204194201" onclick="editor.TogglePrivate('204194201', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204194201" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204194201">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204194201">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204194201" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204194201&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204194201" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204194201">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204194201">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204194201" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204194201&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204194201').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204194201').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204194201", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204194201').tooltip()
            $('#showHistory204194201').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204194201, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204194201, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5162"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    peter
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 8:56am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5162"><span class="hidden-xs">#5162&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204194215">
        <div class="forcebreak" dir="auto"><meta http-equiv="Content-Type">Hi Dan,<div><br></div><div>Biggest comment would be the I’d recommend a “strangler” pattern, rebuilding subsets of the functionality a piece at a time. Despite the risks around data integrity, I’d also consider just keeping the MySQL db and having both apps read/write to it.&nbsp;</div><div><br></div><div>I’d also be super thoughtful about the business risk of messing things up. At the most basic, make sure you have at a very least daily backups and a tested and working recovery process in the case of data loss.</div><div>I’d also consider replicating production to staging for the current app so you have a production like environment for testing</div><div>I might even consider running tests where the new and old staging servers mirror each other and confirm responses to make sure they match - works well for legacy code with limited test coverage and specs</div><div><br></div><div>Definitely a very big lift, try to break it into lots of modest wins.</div><div><br></div><div>Best Wishes,</div><div>Peter</div><div><br></div><div><br><div></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204194215" role="button" data-toggle="collapse" href="#quoted-204194215" aria-expanded="false" aria-controls="quoted-204194215"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204194215" class="collapse forcebreak">
            <div dir="auto"><blockquote><div>On Apr 26, 2022, at 11:27 AM, Dan Richards &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:</div><br class="Apple-interchange-newline"><div>
  

    <meta http-equiv="content-type">
  
  <div>
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre class="moz-signature">-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a class="moz-txt-link-abbreviated" href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div>



  

</div></blockquote><br></div>
          </div>
          <script>
            $('#quoted-204194215').on('show.bs.collapse', function () {
              $('#qlabel-204194215').text("Hide quoted text");
            })
            $('#quoted-204194215').on('hide.bs.collapse', function () {
              $('#qlabel-204194215').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204194215" aria-expanded="false" aria-controls="window-204194215"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204194215"><span id="likebutton204194215"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204194215, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204194215" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204194215">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388246"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204194215"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204194215"><span id="likestats204194215"></span></div>
        </div>
      </div>
      
        <div id="window-204194215" class="collapse">
          <form class="form" id="form204194215" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204194215" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204194215">
            <input type="hidden" id="groupname204194215" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204194215" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204194215" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204194215" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204194215">
    <textarea id="editor204194215" name="editor204194215" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204194215"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204194215"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204194215" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204194215" value="html">
              

              <div id="bccme204194215" class="checkbox">
                <label for="bccme204194215">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204194215" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204194215"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204194215" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204194215" name="preview" onclick="editor.PreviewMarkdown(204194215,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204194215" name="return" onclick="editor.ReturnMarkdown(204194215)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204194215" data-toggle="collapse" data-target="#window-204194215"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204194215" onclick="editor.TogglePrivate('204194215', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204194215" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204194215">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204194215">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204194215" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204194215&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204194215" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204194215">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204194215">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204194215" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204194215&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204194215').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204194215').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204194215", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204194215').tooltip()
            $('#showHistory204194215').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204194215, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204194215, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5163"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
		
			<a href="/g/worldwide/profile/@speby">Sean Eby</a>
		
  

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 8:57am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5163"><span class="hidden-xs">#5163&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204194266">
        <div class="forcebreak" dir="auto"><meta http-equiv="Content-Type"><span style=" color: rgb(0, 0, 0);">Dan,</span><div style=" color: rgb(0, 0, 0);"><br></div><div style=" color: rgb(0, 0, 0);">ALL of these are great questions and no doubt something I am sure numerous people in here have faced before, myself included. For a “rebuild” decision, it helps to start with truly understanding what the underlying problems are. Some of which could include but certainly not limited to:</div><div style=" color: rgb(0, 0, 0);"><br></div><div style=" color: rgb(0, 0, 0);"><ul class="MailOutline"><li>Just a really old codebase, perhaps on a frame work that is either dying or is dead/no-longer-maintained. In the PHP world, that might be, say, a CodeIgniter web app.</li><li>A code base that had very little oversight and less skilled people working on it for years on end, leading to a “ball of mud” as it sometimes might get called, with heavy amounts of hard-coding (e.g. huge amounts of hard-coded SQL, for example), little to no reuse, catch-all classes/models/controllers, etc.</li><li>Because of the above potential issues, overall maintenance of the app being a huge source of pain is also a struggle.</li><li>Recruiting/talent can also be a factor, particularly if the company is in a growth stage and innovation is important. A COBOL app at a bank, for example, might be “OK” in terms of its codebase but let’s be honest, you’re not exactly out recruiting people who want and can work on that to come in and do some more ground-breaking and/or new product innovation. It’s just not there.</li><li>… and of course there are numerous other factors besides.</li></ul><div><br></div><div>For a rebuild to make sense and to even support the business case behind it, I find it is generally helpful if it also coincides with another effort that you/the business want to achieve. For example, let’s say the UI/UX of the app is aging, the business and customers know it, and there is real desire to invest in significantly revamping and transforming the UI/UX of the product for the next 5-7 years of its life. That could be a great project to use as a foundation for why a rebuild might make sense to do in conjunction with it. Besides the issues I mentioned above, it also could be the case that the view/presentation layer of the app, and all of the CSS, etc. is a total mess, and thus “revamping” the UI/UX of it does not really make sense with the current codebase, thus serious consideration to a rebuild is not out of the question, and could support your business case behind doing so.</div><div><br></div><div>On PHP, while I myself don’t have strong negative opinions of PHP, it also isn’t something greatly excites me. But it’s not so bad a reputation that I’d argue ripping it all out and replacing it with a cool new kid like Elixir or Go or something. From a recruiting standpoint, there is plenty of enthusiastic talent in PHP so honestly recruiting is not and has not been a challenge and I’ve led teams that work predominantly with it for use with backend APIs, etc.</div><div><br></div><div>In 2022, building from scratch, while I do think PHP/Laravel as a combo is a viable choice, there are now so many other great choices as well. But ‘from scratch’ in my mind usually refers to starting either a brand new product from scratch or starting a new company from scratch and thinking thru which tech stack you think you would want to marry. SeanG has good points about PHP maybe not being the first choice and I agree. But I will say it is a viable one and if I had a large team that mostly already understood and used PHP, I feel it would be a difficult case to say let’s just switch everybody over to something else just cuz.</div><div><br></div><div>Also, as others have now mentioned on this thread, the strangler pattern is good potential path for doing a rebuild. Just know, like you already said, it’s going to be a long path…. years, at least. Based on what you’ve shared.</div></div><div>
—<div>Sean Eby</div><div><a href="mailto:sean.eby@gmail.com" rel="nofollow noopener" target="_blank">sean.eby@gmail.com</a></div><div>+1.847.903.1311</div>
</div>
<div><br></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204194266" role="button" data-toggle="collapse" href="#quoted-204194266" aria-expanded="false" aria-controls="quoted-204194266"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204194266" class="collapse forcebreak">
            <div dir="auto"><blockquote><div>On Apr 26, 2022, at 9:53 AM, Sean Goodpasture &lt;<a href="mailto:goofygrin@gmail.com" rel="nofollow noopener" target="_blank">goofygrin@gmail.com</a>&gt; wrote:</div><br class="Apple-interchange-newline"><div><div dir="ltr">A bit tongue in cheek, but I agree with your instincts...<div><br></div><div>10 years to build - 10 years to rebuild</div><div><br></div><div>I would pick a more modern stack and language (and go far more cloud native).&nbsp; There's too many options here, but I would pick something more accessible like nodejs or java as it will lower the TCO.</div><div><br></div><div>PHP/Laravel?&nbsp; No, never.&nbsp; Certainly not in 2022.</div><div><br></div><div>Having done this the wrong way a bunch, the most successful pattern (which as you point out is still fraught with risks) I've used &amp; seen is the strangler pattern (<a href="https://www.castsoftware.com/blog/how-to-use-strangler-pattern-for-microservices-modernization" rel="nofollow noopener" target="_blank">https://www.castsoftware.com/blog/how-to-use-strangler-pattern-for-microservices-modernization</a>).&nbsp; It takes even longer to do it this way, but it changes the risk profile completely.</div><div><br></div><div>Sean</div><div><br></div><div><br></div></div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 9:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">
  

    
  
  <div>
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div><div><br class="webkit-block-placeholder"></div><div><br class="webkit-block-placeholder"></div></blockquote></div>


  

</div></blockquote><br></div>
          </div>
          <script>
            $('#quoted-204194266').on('show.bs.collapse', function () {
              $('#qlabel-204194266').text("Hide quoted text");
            })
            $('#quoted-204194266').on('hide.bs.collapse', function () {
              $('#qlabel-204194266').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204194266" aria-expanded="false" aria-controls="window-204194266"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204194266"><span id="likebutton204194266"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204194266, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204194266" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204194266">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:3980719"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204194266"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204194266"><span id="likestats204194266"></span></div>
        </div>
      </div>
      
        <div id="window-204194266" class="collapse">
          <form class="form" id="form204194266" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204194266" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204194266">
            <input type="hidden" id="groupname204194266" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204194266" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204194266" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204194266" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204194266">
    <textarea id="editor204194266" name="editor204194266" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204194266"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204194266"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204194266" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204194266" value="html">
              

              <div id="bccme204194266" class="checkbox">
                <label for="bccme204194266">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204194266" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204194266"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204194266" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204194266" name="preview" onclick="editor.PreviewMarkdown(204194266,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204194266" name="return" onclick="editor.ReturnMarkdown(204194266)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204194266" data-toggle="collapse" data-target="#window-204194266"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204194266" onclick="editor.TogglePrivate('204194266', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204194266" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204194266">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204194266">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204194266" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204194266&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204194266" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204194266">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204194266">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204194266" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204194266&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204194266').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204194266').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204194266", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204194266').tooltip()
            $('#showHistory204194266').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204194266, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204194266, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5164"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    david raistrick
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 9:16am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5164"><span class="hidden-xs">#5164&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204195362">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div dir="ltr">On Tue, Apr 26, 2022 at 11:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:<br></div><div class="gmail_quote"><div>&nbsp;</div><blockquote class="gmail_quote"><div><div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div></div></blockquote><div><br></div><div><br></div><div>You can't magically remove the old codebase instantly (unless it has zero traffic, zero bugs, or needs zero feature work), they're going to have to continue to support the PHP stack.&nbsp; So switching languages will only complicate the problem.</div><div><br></div><div>There are plenty of folks still using php - for new and existing projects.&nbsp;</div><div><br></div><div><br></div><blockquote class="gmail_quote"><div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div></div></blockquote><div><br></div><div>I'd start such a consideration with the team in mind.&nbsp; &nbsp;If the current team are heavily invested in PHP, and you show up with a new team writing Java, is the old team going to feel like it's time to walk?&nbsp; &nbsp; Maybe the team wants to try something new, so start with some POC projects based on the teams interest?</div><div><br></div><div>IMO, language doesn't matter.&nbsp; The team does.&nbsp;&nbsp;</div><div><br></div><div>If this is a company without a team, then obviously it's a different starting point - but it's just as important to consider since you still can't remove the legacy product.</div><div><br></div><div><br></div><blockquote class="gmail_quote"><div><div>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br></div></div></blockquote><div><br></div><div>Everything comes with compatibility changes, and everything makes the process longer.&nbsp; &nbsp;The other tongue-in-cheek suggestion of "it took 10 years to write the first one, it'll take 10 years to write the next one" isn't wrong.&nbsp; But -&nbsp;</div><div><br></div><div>It's 2022 - we need to stop looking at software as something we write once and "finish" with.&nbsp; &nbsp;&nbsp;</div><div><br></div><div>Even packaged applications - which isn't what we're talking about here - need maintenance and rewrites.</div><div><br></div><div>Software the runs live in front of customers?&nbsp; It's never "done" - so don't try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company folded and the IP got lost in the shareholder fight"</div><div><br></div><div>A growing product will need changes - to the legacy codebase, and the new codebase.</div><div><br></div><div>There are very few products that have "servers" and "databases" that can do 100% rebuild lift and shifts.&nbsp; &nbsp;Those that can generally don't have infra.</div><div><br></div><div>This sounds like a great time to help the client see the value in re-thinking how they view their company - they're in the software business, they're selling software.&nbsp; &nbsp;They're a software business.&nbsp; Refocus!</div><div><br></div><div>...david</div><blockquote class="gmail_quote"> 

<p></p><p></p></blockquote></div></div></div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204195362" aria-expanded="false" aria-controls="window-204195362"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204195362"><span id="likebutton204195362"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204195362, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204195362" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204195362">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:231388"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204195362"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204195362"><span id="likestats204195362"></span></div>
        </div>
      </div>
      
        <div id="window-204195362" class="collapse">
          <form class="form" id="form204195362" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204195362" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204195362">
            <input type="hidden" id="groupname204195362" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204195362" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204195362" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204195362" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204195362">
    <textarea id="editor204195362" name="editor204195362" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204195362"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204195362"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204195362" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204195362" value="html">
              

              <div id="bccme204195362" class="checkbox">
                <label for="bccme204195362">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204195362" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204195362"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204195362" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204195362" name="preview" onclick="editor.PreviewMarkdown(204195362,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204195362" name="return" onclick="editor.ReturnMarkdown(204195362)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204195362" data-toggle="collapse" data-target="#window-204195362"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204195362" onclick="editor.TogglePrivate('204195362', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204195362" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204195362">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204195362">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204195362" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204195362&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204195362" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204195362">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204195362">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204195362" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204195362&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204195362').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204195362').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204195362", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204195362').tooltip()
            $('#showHistory204195362').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204195362, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204195362, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5165"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Sean Goodpasture
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 9:23am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5165"><span class="hidden-xs">#5165&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204195766">
        <div class="forcebreak" dir="auto"><div dir="ltr">David,&nbsp;<div><br></div><div>You took the words out of my mouth - the company is actually two - their current core business and a software company.&nbsp; If they want to be truly successful they need to run the software as a product company and drive that way.</div><div><br></div><div>There's lots of positives to spinning it as a separate entity/subsidiary...<br><div><br></div><div>Sean</div></div></div></div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204195766" aria-expanded="false" aria-controls="window-204195766"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204195766"><span id="likebutton204195766"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204195766, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204195766" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204195766">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4125372"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204195766"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204195766"><span id="likestats204195766"></span></div>
        </div>
      </div>
      
        <div id="window-204195766" class="collapse">
          <form class="form" id="form204195766" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204195766" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204195766">
            <input type="hidden" id="groupname204195766" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204195766" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204195766" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204195766" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204195766">
    <textarea id="editor204195766" name="editor204195766" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204195766"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204195766"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204195766" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204195766" value="html">
              

              <div id="bccme204195766" class="checkbox">
                <label for="bccme204195766">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204195766" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204195766"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204195766" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204195766" name="preview" onclick="editor.PreviewMarkdown(204195766,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204195766" name="return" onclick="editor.ReturnMarkdown(204195766)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204195766" data-toggle="collapse" data-target="#window-204195766"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204195766" onclick="editor.TogglePrivate('204195766', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204195766" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204195766">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204195766">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204195766" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204195766&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204195766" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204195766">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204195766">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204195766" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204195766&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204195766').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204195766').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204195766", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204195766').tooltip()
            $('#showHistory204195766').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204195766, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204195766, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5166"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Rajiv Menon
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 9:39am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5166"><span class="hidden-xs">#5166&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204196626">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div dir="ltr">Dan,<div>Good questions. My team at <a href="https://informulate.com/" rel="nofollow noopener" target="_blank">Informulate</a> has a lot of experience (16+ years) converting/migrating legacy applications (esp. PHP/Laravel and .NET). We've probably hit every branch on the&nbsp;Surprise Tree, and its certainly not trivial to balance current state and future state. To answer your&nbsp;questions:</div><div><ol><li>How do you convey and get the business to really understand what it will take to re-build a large complicated web application that has 10+ years of code, business logic, etc.?&nbsp;</li><ul><li>We usually start with some assessments. Code review, bug listing, known system limitations, security/performance concerns, UX, and the unnecessary complexity /inertia of building in the old system are valid points. At the end of the day, its&nbsp;probably more of a business decision than a technical one. So we generally recommend a value proposition mapping exercise to really understand the client's trajectory and building a business case.&nbsp;</li></ul><li>If you were going to re-build - basically build a new web application with a decent amount of financial data, what languages/dbs would you look to be using?</li><ul><li>Others have answered this well enough. Today, I'd recommend full stack JS&nbsp;</li></ul><li>Besides being a bit antiquated, I have stressed that recruiting developers for PHP work may be challenging, thoughts on this?&nbsp; Is this worth switching languages for? They have to hire new staff to do the re-build and it seems a bit short sighted to only look at PHP developers...</li><ul><li>There is a massive installed base of PHP developers. That said, I'd look at full stack JS.&nbsp;</li></ul><li>In 2022, would you even consider building from a scratch a large complicated web app in PHP/Laraval?</li><ul><li>Sure, there are business scenarios where that makes sense. But it needs a deeper dive on the business side to understand what problems are being solved. More importantly, why is this custom solution that important? Is the IP you build worth anything? If it can be monetized then its a slam dunk to do. Is it core to their unique competitive advantage? If not, take another look at packaged apps and do some Product Tank/G2 searches.&nbsp;</li></ul><li><span style="background-color:rgb(255,255,255);  font-family:Arial,Helvetica,sans-serif;  font-size:small;  font-style:normal;  font-weight:normal;  color:rgb(34,34,34);">Would you prefer a "re-build while flying" or build it all new and rollout the new one separately approach?&nbsp; I like </span>re-build<br></li><ul><li>My preference is to rebuild while flying (potentially higher cost and longer timeline, but lower business risk). Technically there are creative ways to rebuild while flying. For one client, we upgraded feature by feature while keeping the database the same, and finally upgraded the database too. In other case, we rebuilt from scratch because it needed to be a clean cutover. Internal facing features can be piece-mealed, externally you want a clean cutover. In some situations, it may make sense to upgrade the back-end gradually (because that is where the biggest risk often is) and then do a clean cutover on the front. It depends on the business needs.&nbsp;</li></ul></ol><div>Happy to jump on a call to discuss more if you need.&nbsp;</div></div><div><br></div><div>All the best!</div><div><br></div><div>-Rajiv</div><div><br></div><div><br></div><div><br></div></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204196626" role="button" data-toggle="collapse" href="#quoted-204196626" aria-expanded="false" aria-controls="quoted-204196626"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204196626" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 12:16 PM david raistrick &lt;<a href="mailto:keen@icantclick.org" rel="nofollow noopener" target="_blank">keen@icantclick.org</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div dir="ltr"><div dir="ltr">On Tue, Apr 26, 2022 at 11:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>&gt; wrote:<br></div><div class="gmail_quote"><div>&nbsp;</div><blockquote class="gmail_quote"><div><div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div></div></blockquote><div><br></div><div><br></div><div>You can't magically remove the old codebase instantly (unless it has zero traffic, zero bugs, or needs zero feature work), they're going to have to continue to support the PHP stack.&nbsp; So switching languages will only complicate the problem.</div><div><br></div><div>There are plenty of folks still using php - for new and existing projects.&nbsp;</div><div><br></div><div><br></div><blockquote class="gmail_quote"><div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div></div></blockquote><div><br></div><div>I'd start such a consideration with the team in mind.&nbsp; &nbsp;If the current team are heavily invested in PHP, and you show up with a new team writing Java, is the old team going to feel like it's time to walk?&nbsp; &nbsp; Maybe the team wants to try something new, so start with some POC projects based on the teams interest?</div><div><br></div><div>IMO, language doesn't matter.&nbsp; The team does.&nbsp;&nbsp;</div><div><br></div><div>If this is a company without a team, then obviously it's a different starting point - but it's just as important to consider since you still can't remove the legacy product.</div><div><br></div><div><br></div><blockquote class="gmail_quote"><div><div>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br></div></div></blockquote><div><br></div><div>Everything comes with compatibility changes, and everything makes the process longer.&nbsp; &nbsp;The other tongue-in-cheek suggestion of "it took 10 years to write the first one, it'll take 10 years to write the next one" isn't wrong.&nbsp; But -&nbsp;</div><div><br></div><div>It's 2022 - we need to stop looking at software as something we write once and "finish" with.&nbsp; &nbsp;&nbsp;</div><div><br></div><div>Even packaged applications - which isn't what we're talking about here - need maintenance and rewrites.</div><div><br></div><div>Software the runs live in front of customers?&nbsp; It's never "done" - so don't try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company folded and the IP got lost in the shareholder fight"</div><div><br></div><div>A growing product will need changes - to the legacy codebase, and the new codebase.</div><div><br></div><div>There are very few products that have "servers" and "databases" that can do 100% rebuild lift and shifts.&nbsp; &nbsp;Those that can generally don't have infra.</div><div><br></div><div>This sounds like a great time to help the client see the value in re-thinking how they view their company - they're in the software business, they're selling software.&nbsp; &nbsp;They're a software business.&nbsp; Refocus!</div><div><br></div><div>...david</div><blockquote class="gmail_quote"> 

<p></p><p></p></blockquote></div></div>


  

<p></p><p></p></blockquote></div><br><div><br></div></div>
          </div>
          <script>
            $('#quoted-204196626').on('show.bs.collapse', function () {
              $('#qlabel-204196626').text("Hide quoted text");
            })
            $('#quoted-204196626').on('hide.bs.collapse', function () {
              $('#qlabel-204196626').text("Show quoted text");
            })
          </script>
        
        
          <div class="forcebreak" dir="auto">-- <br><div dir="ltr" class="gmail_signature"><div dir="ltr"><div><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div><div><div><div><div><div><br></div></div></div></div></div></div><div><table><tbody><tr><td><img src="https://informulate.com/email_signatures/Final-Version.png" alt="Informulate" height="87" width="200" class="myimg-responsive"></td><td><p><strong>Rajiv Menon</strong></p><table><tbody><tr><td><img src="https://informulate.com/email_signatures/glyphicons-443-earphone@3x.png" alt="Phone" class="myimg-responsive"></td><td><a href="tel:+18662222307" target="_blank" rel="nofollow noopener">866-222-2307</a></td></tr><tr><td><img src="https://informulate.com/email_signatures/glyphicons-11-envelope@3x.png" alt="Mail" class="myimg-responsive"></td><td><a href="mailto:rajiv.menon@informulate.com" target="_blank" rel="nofollow noopener">rajiv.menon@informulate.com</a></td></tr><tr><td><img src="https://informulate.com/email_signatures/glyphicons-372-global@3x.png" alt="Web" class="myimg-responsive"></td><td><a href="https://informulate.com/" target="_blank" rel="nofollow noopener">www.Informulate.com</a></td></tr></tbody></table><table><tbody><tr><td><a href="https://www.facebook.com/Informulate" target="_blank" rel="nofollow noopener"><img src="https://informulate.com/email_signatures/glyphicons-social-31-facebook@3x.png" class="myimg-responsive"></a></td><td><a href="https://twitter.com/Informulate" target="_blank" rel="nofollow noopener"><img src="https://informulate.com/email_signatures/glyphicons-social-32-twitter@3x.png" class="myimg-responsive"></a></td><td><a href="https://www.linkedin.com/company/informulate-llc/" target="_blank" rel="nofollow noopener"><img src="https://informulate.com/email_signatures/glyphicons-social-18-linked-in@3x.png" class="myimg-responsive"></a></td></tr></tbody></table></td></tr></tbody></table></div><div><br></div><div><table><tbody><tr><td width="576" colspan="2"><p style="font-size:11pt;  font-family:Helvetica;"><span style="font-size:8pt;  color:rgb(85,85,85);">Curious how our <a href="https://www.youtube.com/watch?v=E2xwpgMZghk" target="_blank" rel="nofollow noopener">software solutions</a> can impact your business?&nbsp;</span></p><p style="font-size:11pt;  font-family:Helvetica;"><span style="font-size:8pt;  color:rgb(85,85,85);">Schedule a discovery consultation.&nbsp;<a href="https://www.calendly.com/rajiv-menon" target="_blank" rel="nofollow noopener">click here</a></span></p><p style="font-size:11pt;  font-family:Helvetica;"><a href="https://orlando.org/l/newsletter-sign-up/" target="_blank" rel="nofollow noopener"></a><br></p><div><br></div></td></tr></tbody></table></div><div><p></p></div></div></div></div></div></div></div></div></div><img src="https://t.sidekickopen90.com/s3t/o/5/f18dQhb0S7n28bNNhRW7zKg8R1jkhdLW1_k-L-1qZXc5N3s0w0r6bdQkDJFjXW-KtLdNJcdH03?si=7000000001024244&amp;pi=81d4714f-6828-4414-8530-50ff8849cebb" alt="" style="" height="1" width="1" class="myimg-responsive"><div></div></div>
        
        
      </div>

      
        <p>
        </p><div class="row">
          
            <div class="col-md-2">
              <div class="thumbnail">
                <a href="https://ctolunches.groups.io/g/worldwide/attachment/5166/0/image002.jpg">
                
                  <img src="https://s3-us-west-1.amazonaws.com/groupsioattachments/23895/90710568/5166/0?AWSAccessKeyId=AKIAJECNKOVMCCU3ATNQ&amp;Expires=1651650871&amp;Signature=%2F5UBCCVwbWiyLpFtOVdK%2FqKSNxA%3D" style="max-width:215;max-height:215">
                
                </a>
              </div>
            </div>
          
        </div>
      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204196626" aria-expanded="false" aria-controls="window-204196626"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204196626"><span id="likebutton204196626"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204196626, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204196626" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204196626">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1837251"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204196626"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204196626"><span id="likestats204196626"></span></div>
        </div>
      </div>
      
        <div id="window-204196626" class="collapse">
          <form class="form" id="form204196626" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204196626" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204196626">
            <input type="hidden" id="groupname204196626" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204196626" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204196626" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204196626" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204196626">
    <textarea id="editor204196626" name="editor204196626" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204196626"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204196626"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204196626" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204196626" value="html">
              

              <div id="bccme204196626" class="checkbox">
                <label for="bccme204196626">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204196626" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204196626"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204196626" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204196626" name="preview" onclick="editor.PreviewMarkdown(204196626,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204196626" name="return" onclick="editor.ReturnMarkdown(204196626)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204196626" data-toggle="collapse" data-target="#window-204196626"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204196626" onclick="editor.TogglePrivate('204196626', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204196626" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204196626">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204196626">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204196626" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204196626&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204196626" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204196626">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204196626">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204196626" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204196626&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204196626').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204196626').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204196626", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204196626').tooltip()
            $('#showHistory204196626').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204196626, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204196626, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5167"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <img src="https://ctolunches.groups.io/g/worldwide/profilephoto/3113920" width="40" height="40" class="img-rounded">
    
    
  
	
		
			<a href="/g/worldwide/profile/@wickedsmaht">Jason Cole</a>
		
  

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 9:52am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5167"><span class="hidden-xs">#5167&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204197327">
        <div class="forcebreak" dir="auto"><meta http-equiv="Content-Type">First, this conversation has already given me some great quotes/war stories that I need to hear:<div><br></div><div><blockquote>I've seen it done well maybe twice? But with a lot more failures (including a CTO telling me he could re-build the entire 15 year old codebase in .NET in three weeks—he did not succeed).</blockquote><div>
<div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">— Kendall Miller</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><blockquote>Software the runs live in front of customers?&nbsp; It's never "done" - so don't try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company folded and the IP got lost in the shareholder fight"</blockquote></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">— David Raistrick</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">Yeah, I’m definitely using that second one the next time someone asks me when we can stop working on our software.</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">Now, a few additional thoughts:</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br></div><div style="text-align: start;"><b>"10 years to build = 10 years to rebuild”</b></div><div style="text-align: start;">I know this was kind of a joke, and I know from experience that it can sometimes feel true, but I want to add one modifier here. It’s probably more like “20 person years to build = 15 person years to rebuild.” An “accidental SaaS” product like this often starts with one engineer futzing around trying to solve a problem, then a team accreting around them over the years like barnacles on a shipwreck. Now you look at the team and your brain extends the entire team back to the beginning. A lot of that early work was either pretty simple or it’s been rewritten, so it’s not quite that bad. There’s also a ton of hidden business logic in there, though, so even if you think you know what it’s doing, you don’t, and you’ll need to rediscover it as you go. How much has the team grown in the past few years?</div><div style="text-align: start;"><br></div><div style="text-align: start;"><b>What’s the core value?&nbsp;</b></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">Over the past ten years, the business and the software have evolved, so it’s possible that you don’t need to rebuild the current product, but rather to build a new product that meets today’s needs. What’s that core value? Can you carve that part off, offer it as a new version, and migrate customers over? Then you don’t have to try to figure out why it does that thing that Bob wrote 9 1/2 years ago: you can build a new product that does what customers need today. This is still a major effort and will probably take a couple of years, but if the business has changed significantly then it might be a better option. Then you’re free to make whatever tech choices you want while putting the current product in maintenance mode.</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><b>Tech choices</b></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">I’m with David: a productive team is more important than the tech stack, but the ability to build a productive team often depends upon using technology that productive people want to use. As languages age, the dynamics of the teams that work on them change. Mature technologies tend to have more mature people working with them, as the youngest (at heart) engineers move on to the latest toys. As languages age out, you generally go through stages where it gets harder to find people who want to work in them full-time, then you can only find outsourced companies that specialize in them, then you have to bring someone out of retirement to fix them. PHP is somewhere in the “mature but not dying” stage right now, but if you choose to build/rebuild a large product with it you should think of it as a five-year commitment. Will you be able to build the team you want for the next five years?</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><b>A story</b></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">Reed Group wasn’t an accidental SaaS company, but it definitely wasn’t a software company when I joined, and the early years of the product were driven by some very opinionated clients. When the product was about five years old, a group of people who had been there in the early years formed a competitor with the idea that they could take what they’d learned at Reed Group and build a new and better version of our enterprise product in a year. They had a very light version live in about a year, but their customers were unhappy with all that was missing compared to our full-featured version. It took them three years to create something that was functionally comparable to the product they’d left behind, and they’ve been developing full-speed ever since to keep up with customer requests. So that was approximately a 60% rebuild cost.</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><br class="Apple-interchange-newline"><br></div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">Jason Cole</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);">CEO</div><div style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"><a href="https://www.daprimus.com" rel="nofollow noopener" target="_blank">Da Primus Consulting</a></div><span style="font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;   color: rgb(0, 0, 0);"></span><br class="Apple-interchange-newline"><span style=" color: rgb(0, 0, 0);   font-family: Helvetica;   font-size: 12px;   font-style: normal;   font-weight: normal;   text-align: start;   text-decoration: none;"></span><span><img id="E54AEF94-77E9-4B5E-A5E5-E00C1382E5C6" src="https://s3-us-west-1.amazonaws.com/groupsioattachments/23895/90710568/5167/0?AWSAccessKeyId=AKIAJECNKOVMCCU3ATNQ&amp;Expires=1651650871&amp;Signature=IM%2BGQwePGsfLMCZknDVIYDZaXoE%3D" class="myimg-responsive"></span>
</div>
<div><br><blockquote><div>On Apr 26, 2022, at 10:23 AM, Sean Goodpasture &lt;<a href="mailto:goofygrin@gmail.com" rel="nofollow noopener" target="_blank">goofygrin@gmail.com</a>&gt; wrote:</div><br class="Apple-interchange-newline"><div><div dir="ltr">David,&nbsp;<div><br></div><div>You took the words out of my mouth - the company is actually two - their current core business and a software company.&nbsp; If they want to be truly successful they need to run the software as a product company and drive that way.</div><div><br></div><div>There's lots of positives to spinning it as a separate entity/subsidiary...<br><div><br></div><div>Sean</div></div></div>


  

</div></blockquote></div><br></div></div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204197327" aria-expanded="false" aria-controls="window-204197327"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204197327"><span id="likebutton204197327"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204197327, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204197327" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204197327">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388204"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204197327"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204197327"><span id="likestats204197327"></span></div>
        </div>
      </div>
      
        <div id="window-204197327" class="collapse">
          <form class="form" id="form204197327" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204197327" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204197327">
            <input type="hidden" id="groupname204197327" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204197327" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204197327" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204197327" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204197327">
    <textarea id="editor204197327" name="editor204197327" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204197327"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204197327"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204197327" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204197327" value="html">
              

              <div id="bccme204197327" class="checkbox">
                <label for="bccme204197327">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204197327" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204197327"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204197327" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204197327" name="preview" onclick="editor.PreviewMarkdown(204197327,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204197327" name="return" onclick="editor.ReturnMarkdown(204197327)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204197327" data-toggle="collapse" data-target="#window-204197327"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204197327" onclick="editor.TogglePrivate('204197327', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204197327" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204197327">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204197327">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204197327" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204197327&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204197327" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204197327">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204197327">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204197327" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204197327&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204197327').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204197327').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204197327", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204197327').tooltip()
            $('#showHistory204197327').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204197327, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204197327, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5168"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    jzapin
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 9:53am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5168"><span class="hidden-xs">#5168&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204197397">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div dir="ltr">Definitely great dialogue here.&nbsp;<div><br></div><div>My only $.02 comes from a product perspective.&nbsp;&nbsp;</div><div><br></div><div>In my experience, rebuilding/replatforming usually makes the most&nbsp;sense when you truly rethink the value of the application.&nbsp; I'm sure there are advantages/cost savings to just rebuild.&nbsp; But it becomes more valuable when you improve functionality/usability and/or perhaps finding a new market?&nbsp; Not only does that give the project more opportunity, it can also help with morale of the team itself (especially if it's the internal team doing it).</div><div><br></div><div>JZ<br><div><div dir="ltr"><div dir="ltr"><div><div dir="ltr"><div><div dir="ltr"><div dir="ltr"><div dir="ltr"><div><br></div><div dir="ltr"><span style="color:rgb(136,136,136);  font-family:arial;">M:&nbsp;(303) 506-8262</span><div style="color:rgb(136,136,136);  font-family:arial;"><a href="http://linkedin.com/in/jzapin" target="_blank" rel="nofollow noopener">linkedin</a></div></div></div></div></div></div></div></div></div></div></div><br></div></div><br></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204197397" role="button" data-toggle="collapse" href="#quoted-204197397" aria-expanded="false" aria-controls="quoted-204197397"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204197397" class="collapse forcebreak">
            <div dir="auto"><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 10:39 AM Rajiv Menon &lt;<a href="mailto:rajiv.menon@informulate.net" target="_blank" rel="nofollow noopener">rajiv.menon@informulate.net</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div dir="ltr"><div dir="ltr">Dan,<div>Good questions. My team at <a href="https://informulate.com/" target="_blank" rel="nofollow noopener">Informulate</a> has a lot of experience (16+ years) converting/migrating legacy applications (esp. PHP/Laravel and .NET). We've probably hit every branch on the&nbsp;Surprise Tree, and its certainly not trivial to balance current state and future state. To answer your&nbsp;questions:</div><div><ol><li>How do you convey and get the business to really understand what it will take to re-build a large complicated web application that has 10+ years of code, business logic, etc.?&nbsp;</li><ul><li>We usually start with some assessments. Code review, bug listing, known system limitations, security/performance concerns, UX, and the unnecessary complexity /inertia of building in the old system are valid points. At the end of the day, its&nbsp;probably more of a business decision than a technical one. So we generally recommend a value proposition mapping exercise to really understand the client's trajectory and building a business case.&nbsp;</li></ul><li>If you were going to re-build - basically build a new web application with a decent amount of financial data, what languages/dbs would you look to be using?</li><ul><li>Others have answered this well enough. Today, I'd recommend full stack JS&nbsp;</li></ul><li>Besides being a bit antiquated, I have stressed that recruiting developers for PHP work may be challenging, thoughts on this?&nbsp; Is this worth switching languages for? They have to hire new staff to do the re-build and it seems a bit short sighted to only look at PHP developers...</li><ul><li>There is a massive installed base of PHP developers. That said, I'd look at full stack JS.&nbsp;</li></ul><li>In 2022, would you even consider building from a scratch a large complicated web app in PHP/Laraval?</li><ul><li>Sure, there are business scenarios where that makes sense. But it needs a deeper dive on the business side to understand what problems are being solved. More importantly, why is this custom solution that important? Is the IP you build worth anything? If it can be monetized then its a slam dunk to do. Is it core to their unique competitive advantage? If not, take another look at packaged apps and do some Product Tank/G2 searches.&nbsp;</li></ul><li><span style="background-color:rgb(255,255,255);  font-family:Arial,Helvetica,sans-serif;  font-size:small;  font-style:normal;  font-weight:normal;  color:rgb(34,34,34);  display:inline;">Would you prefer a "re-build while flying" or build it all new and rollout the new one separately approach?&nbsp; I like </span>re-build<br></li><ul><li>My preference is to rebuild while flying (potentially higher cost and longer timeline, but lower business risk). Technically there are creative ways to rebuild while flying. For one client, we upgraded feature by feature while keeping the database the same, and finally upgraded the database too. In other case, we rebuilt from scratch because it needed to be a clean cutover. Internal facing features can be piece-mealed, externally you want a clean cutover. In some situations, it may make sense to upgrade the back-end gradually (because that is where the biggest risk often is) and then do a clean cutover on the front. It depends on the business needs.&nbsp;</li></ul></ol><div>Happy to jump on a call to discuss more if you need.&nbsp;</div></div><div><br></div><div>All the best!</div><div><br></div><div>-Rajiv</div><div><br></div><div><br></div><div><br></div></div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 12:16 PM david raistrick &lt;<a href="mailto:keen@icantclick.org" target="_blank" rel="nofollow noopener">keen@icantclick.org</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div dir="ltr"><div dir="ltr">On Tue, Apr 26, 2022 at 11:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>&gt; wrote:<br></div><div class="gmail_quote"><div>&nbsp;</div><blockquote class="gmail_quote"><div><div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div></div></blockquote><div><br></div><div><br></div><div>You can't magically remove the old codebase instantly (unless it has zero traffic, zero bugs, or needs zero feature work), they're going to have to continue to support the PHP stack.&nbsp; So switching languages will only complicate the problem.</div><div><br></div><div>There are plenty of folks still using php - for new and existing projects.&nbsp;</div><div><br></div><div><br></div><blockquote class="gmail_quote"><div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div></div></blockquote><div><br></div><div>I'd start such a consideration with the team in mind.&nbsp; &nbsp;If the current team are heavily invested in PHP, and you show up with a new team writing Java, is the old team going to feel like it's time to walk?&nbsp; &nbsp; Maybe the team wants to try something new, so start with some POC projects based on the teams interest?</div><div><br></div><div>IMO, language doesn't matter.&nbsp; The team does.&nbsp;&nbsp;</div><div><br></div><div>If this is a company without a team, then obviously it's a different starting point - but it's just as important to consider since you still can't remove the legacy product.</div><div><br></div><div><br></div><blockquote class="gmail_quote"><div><div>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br></div></div></blockquote><div><br></div><div>Everything comes with compatibility changes, and everything makes the process longer.&nbsp; &nbsp;The other tongue-in-cheek suggestion of "it took 10 years to write the first one, it'll take 10 years to write the next one" isn't wrong.&nbsp; But -&nbsp;</div><div><br></div><div>It's 2022 - we need to stop looking at software as something we write once and "finish" with.&nbsp; &nbsp;&nbsp;</div><div><br></div><div>Even packaged applications - which isn't what we're talking about here - need maintenance and rewrites.</div><div><br></div><div>Software the runs live in front of customers?&nbsp; It's never "done" - so don't try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company folded and the IP got lost in the shareholder fight"</div><div><br></div><div>A growing product will need changes - to the legacy codebase, and the new codebase.</div><div><br></div><div>There are very few products that have "servers" and "databases" that can do 100% rebuild lift and shifts.&nbsp; &nbsp;Those that can generally don't have infra.</div><div><br></div><div>This sounds like a great time to help the client see the value in re-thinking how they view their company - they're in the software business, they're selling software.&nbsp; &nbsp;They're a software business.&nbsp; Refocus!</div><div><br></div><div>...david</div><blockquote class="gmail_quote"> 

<p></p><p></p></blockquote></div></div>


  

<p></p><p></p></blockquote></div><br><div><br></div>-- <br><div dir="ltr"><div dir="ltr"><div><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div><div><div><div><div><div><br></div></div></div></div></div></div><div><table><tbody><tr><td><img src="https://informulate.com/email_signatures/Final-Version.png" alt="Informulate" height="87" width="200" class="myimg-responsive"></td><td><p><strong>Rajiv Menon</strong></p><table><tbody><tr><td><img src="https://informulate.com/email_signatures/glyphicons-443-earphone@3x.png" alt="Phone" class="myimg-responsive"></td><td><a href="tel:+18662222307" target="_blank" rel="nofollow noopener">866-222-2307</a></td></tr><tr><td><img src="https://informulate.com/email_signatures/glyphicons-11-envelope@3x.png" alt="Mail" class="myimg-responsive"></td><td><a href="mailto:rajiv.menon@informulate.com" target="_blank" rel="nofollow noopener">rajiv.menon@informulate.com</a></td></tr><tr><td><img src="https://informulate.com/email_signatures/glyphicons-372-global@3x.png" alt="Web" class="myimg-responsive"></td><td><a href="https://informulate.com/" target="_blank" rel="nofollow noopener">www.Informulate.com</a></td></tr></tbody></table><table><tbody><tr><td><a href="https://www.facebook.com/Informulate" target="_blank" rel="nofollow noopener"><img src="https://informulate.com/email_signatures/glyphicons-social-31-facebook@3x.png" class="myimg-responsive"></a></td><td><a href="https://twitter.com/Informulate" target="_blank" rel="nofollow noopener"><img src="https://informulate.com/email_signatures/glyphicons-social-32-twitter@3x.png" class="myimg-responsive"></a></td><td><a href="https://www.linkedin.com/company/informulate-llc/" target="_blank" rel="nofollow noopener"><img src="https://informulate.com/email_signatures/glyphicons-social-18-linked-in@3x.png" class="myimg-responsive"></a></td></tr></tbody></table></td></tr></tbody></table></div><div><br></div><div><table><tbody><tr><td width="576" colspan="2"><p style="font-size:11pt;  font-family:Helvetica;"><span style="font-size:8pt;  color:rgb(85,85,85);">Curious how our <a href="https://www.youtube.com/watch?v=E2xwpgMZghk" target="_blank" rel="nofollow noopener">software solutions</a> can impact your business?&nbsp;</span></p><p style="font-size:11pt;  font-family:Helvetica;"><span style="font-size:8pt;  color:rgb(85,85,85);">Schedule a discovery consultation.&nbsp;<a href="https://www.calendly.com/rajiv-menon" target="_blank" rel="nofollow noopener">click here</a></span></p><p style="font-size:11pt;  font-family:Helvetica;"><a href="https://orlando.org/l/newsletter-sign-up/" target="_blank" rel="nofollow noopener"><img width="200" height="23" class="myimg-responsive"></a><br></p><div><br></div></td></tr></tbody></table></div><div><p></p></div></div></div></div></div></div></div></div></div><img src="https://t.sidekickopen90.com/s3t/o/5/f18dQhb0S7n28bNNhRW7zKg8R1jkhdLW1_k-L-1qZXc5N3s0w0r6bdQkDJFjXW-KtLdNJcdH03?si=7000000001024244&amp;pi=81d4714f-6828-4414-8530-50ff8849cebb" alt="" style="display: none;" height="1" width="1" class="myimg-responsive"><div></div></div>


  

<p></p><p></p></blockquote></div>
<img src="https://t.sidekickopen87.com/s3t/o/5/f18dQhb0S7n28c82jcW5Hx50n2zGCvGW40Fv_62SXv86W6W100T5v0RzFN5v0w2n1tdBSf20NPl-03?si=8000000001907490&amp;pi=54171090-1800-499b-9813-e0941b473a36" alt="" style="" height="1" width="1" class="myimg-responsive"></div>
          </div>
          <script>
            $('#quoted-204197397').on('show.bs.collapse', function () {
              $('#qlabel-204197397').text("Hide quoted text");
            })
            $('#quoted-204197397').on('hide.bs.collapse', function () {
              $('#qlabel-204197397').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204197397" aria-expanded="false" aria-controls="window-204197397"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204197397"><span id="likebutton204197397"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204197397, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204197397" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204197397">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388223"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204197397"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204197397"><span id="likestats204197397"></span></div>
        </div>
      </div>
      
        <div id="window-204197397" class="collapse">
          <form class="form" id="form204197397" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204197397" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204197397">
            <input type="hidden" id="groupname204197397" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204197397" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204197397" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204197397" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204197397">
    <textarea id="editor204197397" name="editor204197397" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204197397"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204197397"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204197397" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204197397" value="html">
              

              <div id="bccme204197397" class="checkbox">
                <label for="bccme204197397">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204197397" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204197397"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204197397" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204197397" name="preview" onclick="editor.PreviewMarkdown(204197397,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204197397" name="return" onclick="editor.ReturnMarkdown(204197397)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204197397" data-toggle="collapse" data-target="#window-204197397"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204197397" onclick="editor.TogglePrivate('204197397', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204197397" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204197397">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204197397">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204197397" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204197397&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204197397" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204197397">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204197397">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204197397" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204197397&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204197397').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204197397').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204197397", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204197397').tooltip()
            $('#showHistory204197397').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204197397, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204197397, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5169"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Miles Cook
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 10:14am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5169"><span class="hidden-xs">#5169&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204198565">
        <div class="forcebreak" dir="auto"><div>Jason has some brilliant points, as well as the person that recommended using the strangler pattern. Used once to great effect to effectively rebuild critical parts of the plane in flight. Oh, and the new vode went to a new DDD folder, which could be ported over to the new API we would build.<div><br></div><div>Its been interesting digesting these points. However, the tech stack? Tools are only as good as the tools using them! Recruitment or finding a good software house plays more of a part in consideration now more than ever.<div><br></div><div>One thing I haven't seen - the why? I&nbsp; an think of a few reasons to rebuild a 10 year old tech stack but my worry would be, everything goes great, flawless migration then.... what did we achieve other than a load of spend? Would just be good to understand what isn't working or a problem on the horizon. If its something specific, that needs to be addressed first.</div><div><br></div><div>Otherwise, no point in my trying to add to some fairly excellent observations in this thread.</div></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204198565" role="button" data-toggle="collapse" href="#quoted-204198565" aria-expanded="false" aria-controls="quoted-204198565"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204198565" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, 26 Apr 2022, 18:52 Jason Cole, &lt;<a href="mailto:jason@daprimus.com" rel="nofollow noopener" target="_blank">jason@daprimus.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div style="">First, this conversation has already given me some great quotes/war stories that I need to hear:<div><br></div><div><blockquote>I've seen it done well maybe twice? But with a lot more failures (including a CTO telling me he could re-build the entire 15 year old codebase in .NET in three weeks—he did not succeed).</blockquote><div>
<div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">— Kendall Miller</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><blockquote>Software the runs live in front of customers?&nbsp; It's never "done" - so don't try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company folded and the IP got lost in the shareholder fight"</blockquote></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">— David Raistrick</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Yeah, I’m definitely using that second one the next time someone asks me when we can stop working on our software.</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Now, a few additional thoughts  :</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br></div><div style="text-align:start;"><b>"10 years to build = 10 years to rebuild”</b></div><div style="text-align:start;">I know this was kind of a joke, and I know from experience that it can sometimes feel true, but I want to add one modifier here. It’s probably more like “20 person years to build = 15 person years to rebuild.” An “accidental SaaS” product like this often starts with one engineer futzing around trying to solve a problem, then a team accreting around them over the years like barnacles on a shipwreck. Now you look at the team and your brain extends the entire team back to the beginning. A lot of that early work was either pretty simple or it’s been rewritten, so it’s not quite that bad. There’s also a ton of hidden business logic in there, though, so even if you think you know what it’s doing, you don’t, and you’ll need to rediscover it as you go. How much has the team grown in the past few years?</div><div style="text-align:start;"><br></div><div style="text-align:start;"><b>What’s the core value?&nbsp;</b></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Over the past ten years, the business and the software have evolved, so it’s possible that you don’t need to rebuild the current product, but rather to build a new product that meets today’s needs. What’s that core value? Can you carve that part off, offer it as a new version, and migrate customers over? Then you don’t have to try to figure out why it does that thing that Bob wrote 9 1/2 years ago: you can build a new product that does what customers need today. This is still a major effort and will probably take a couple of years, but if the business has changed significantly then it might be a better option. Then you’re free to make whatever tech choices you want while putting the current product in maintenance mode.</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><b>Tech choices</b></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">I’m with David: a productive team is more important than the tech stack, but the ability to build a productive team often depends upon using technology that productive people want to use. As languages age, the dynamics of the teams that work on them change. Mature technologies tend to have more mature people working with them, as the youngest (at heart) engineers move on to the latest toys. As languages age out, you generally go through stages where it gets harder to find people who want to work in them full-time, then you can only find outsourced companies that specialize in them, then you have to bring someone out of retirement to fix them. PHP is somewhere in the “mature but not dying” stage right now, but if you choose to build/rebuild a large product with it you should think of it as a five-year commitment. Will you be able to build the team you want for the next five years?</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><b>A story</b></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Reed Group wasn’t an accidental SaaS company, but it definitely wasn’t a software company when I joined, and the early years of the product were driven by some very opinionated clients. When the product was about five years old, a group of people who had been there in the early years formed a competitor with the idea that they could take what they’d learned at Reed Group and build a new and better version of our enterprise product in a year. They had a very light version live in about a year, but their customers were unhappy with all that was missing compared to our full-featured version. It took them three years to create something that was functionally comparable to the product they’d left behind, and they’ve been developing full-speed ever since to keep up with customer requests. So that was approximately a 60% rebuild cost.</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br><br></div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Jason Cole</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">CEO</div><div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><a href="https://www.daprimus.com" target="_blank" rel="nofollow noopener">Da Primus Consulting</a></div><span style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"></span><br><span style="color:rgb(0,0,0);  font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;"></span><span></span>
</div>
<div><br><blockquote><div>On Apr 26, 2022, at 10:23 AM, Sean Goodpasture &lt;<a href="mailto:goofygrin@gmail.com" target="_blank" rel="nofollow noopener">goofygrin@gmail.com</a>&gt; wrote:</div><br><div><div dir="ltr">David,&nbsp;<div><br></div><div>You took the words out of my mouth - the company is actually two - their current core business and a software company.&nbsp; If they want to be truly successful they need to run the software as a product company and drive that way.</div><div><br></div><div>There's lots of positives to spinning it as a separate entity/subsidiary...<br><div><br></div><div>Sean</div></div></div>


  

</div></blockquote></div><br></div></div>


  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204198565').on('show.bs.collapse', function () {
              $('#qlabel-204198565').text("Hide quoted text");
            })
            $('#quoted-204198565').on('hide.bs.collapse', function () {
              $('#qlabel-204198565').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
        <p>
        </p><div class="row">
          
            <div class="col-md-2">
              <div class="thumbnail">
                <a href="https://ctolunches.groups.io/g/worldwide/attachment/5169/0/Da Primus Logos Small-4.png">
                
                  <img src="https://s3-us-west-1.amazonaws.com/groupsioattachments/23895/90710568/5169/0?AWSAccessKeyId=AKIAJECNKOVMCCU3ATNQ&amp;Expires=1651650871&amp;Signature=%2B860xwbWZUhPX3Y%2Fila8ucpC%2Fak%3D" style="max-width:215;max-height:215">
                
                </a>
              </div>
            </div>
          
            <div class="col-md-2">
              <div class="thumbnail">
                <a href="https://ctolunches.groups.io/g/worldwide/attachment/5169/1/Da Primus Logos Small-4.png">
                
                  <img src="https://s3-us-west-1.amazonaws.com/groupsioattachments/23895/90710568/5169/1?AWSAccessKeyId=AKIAJECNKOVMCCU3ATNQ&amp;Expires=1651650871&amp;Signature=0gYWxn%2B7BgRH8ksPnkEEmpsoClA%3D" style="max-width:215;max-height:215">
                
                </a>
              </div>
            </div>
          
        </div>
      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204198565" aria-expanded="false" aria-controls="window-204198565"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204198565"><span id="likebutton204198565"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204198565, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204198565" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204198565">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4752701"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204198565"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204198565"><span id="likestats204198565"></span></div>
        </div>
      </div>
      
        <div id="window-204198565" class="collapse">
          <form class="form" id="form204198565" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204198565" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204198565">
            <input type="hidden" id="groupname204198565" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204198565" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204198565" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204198565" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204198565">
    <textarea id="editor204198565" name="editor204198565" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204198565"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204198565"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204198565" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204198565" value="html">
              

              <div id="bccme204198565" class="checkbox">
                <label for="bccme204198565">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204198565" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204198565"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204198565" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204198565" name="preview" onclick="editor.PreviewMarkdown(204198565,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204198565" name="return" onclick="editor.ReturnMarkdown(204198565)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204198565" data-toggle="collapse" data-target="#window-204198565"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204198565" onclick="editor.TogglePrivate('204198565', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204198565" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204198565">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204198565">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204198565" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204198565&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204198565" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204198565">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204198565">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204198565" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204198565&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204198565').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204198565').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204198565", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204198565').tooltip()
            $('#showHistory204198565').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204198565, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204198565, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5170"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Dan Richards
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 10:33am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5170"><span class="hidden-xs">#5170&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204199615">
        <div class="forcebreak" dir="auto"><meta http-equiv="Content-Type">
  
  
    Man, this group rocks sometimes, doesn't it?<br>
    <br>
    Great feedback from everyone, I really appreciate it.&nbsp;&nbsp; I framed
    this question because my role here is really as a trusted voice to
    the CEO and he knows I won't sell him a bunch of bullshit.&nbsp; He is
    NOT a software person, and knows that he doesn't know, which is why
    he has me. I mostly stay out of the the day-to-day process, so I
    don't have much vested in the team directly.&nbsp; So in this case my
    goal is simply to make sure he knows what kind of stuff he's about
    to step in on embarking on a project like this.&nbsp; As you all shared,
    it is much easier said than done!<br>
    <br>
    For those that speculated, the rationale driving this is the lure of
    larger clients with more demands, more data, etc. which obviously
    taxes and stresses the architecture, infrastructure, etc.<br>
    <br>
    Thanks everyone!<br>
    -Dan<br>
    <br>
    <div class="moz-cite-prefix">On 4/26/22 1:13 PM, Miles Cook via
      groups.io wrote:<br>
    </div>
    <blockquote cite="mid:CAJwdhwBPzvFLKDC3t6x_cq61HEXok+DsaiHQfZbpVrOHvmTebQ@mail.gmail.com">
      <meta http-equiv="Content-Type">
      <div>Jason has some brilliant points, as well as the
        person that recommended using the strangler pattern. Used once
        to great effect to effectively rebuild critical parts of the
        plane in flight. Oh, and the new vode went to a new DDD folder,
        which could be ported over to the new API we would build.
        <div><br>
        </div>
        <div>Its been interesting digesting these points.
          However, the tech stack? Tools are only as good as the tools
          using them! Recruitment or finding a good software house plays
          more of a part in consideration now more than ever.
          <div><br>
          </div>
          <div>One thing I haven't seen - the why? I&nbsp; an
            think of a few reasons to rebuild a 10 year old tech stack
            but my worry would be, everything goes great, flawless
            migration then.... what did we achieve other than a load of
            spend? Would just be good to understand what isn't working
            or a problem on the horizon. If its something specific, that
            needs to be addressed first.</div>
          <div><br>
          </div>
          <div>Otherwise, no point in my trying to add to
            some fairly excellent observations in this thread.</div>
        </div>
      </div>
      <br>
      <div class="gmail_quote">
        <div dir="ltr" class="gmail_attr">On Tue, 26 Apr 2022, 18:52
          Jason Cole, &lt;<a href="mailto:jason@daprimus.com" class="moz-txt-link-freetext" rel="nofollow noopener" target="_blank">jason@daprimus.com</a>&gt;
          wrote:<br>
        </div>
        <blockquote class="gmail_quote">
          <div style="">First,
            this conversation has already given me some great quotes/war
            stories that I need to hear:
            <div><br>
            </div>
            <div>
              <blockquote>I've seen it done well maybe
                twice? But with a lot more failures (including a CTO
                telling me he could re-build the entire 15 year old
                codebase in .NET in three weeks—he did not succeed).</blockquote>
              <div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">—
                  Kendall Miller</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">
                  <blockquote>Software the runs live in
                    front of customers?&nbsp; It's never "done" - so don't
                    try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company
                    folded and the IP got lost in the shareholder fight"</blockquote>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">—
                  David Raistrick</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Yeah,
                  I’m definitely using that second one the next time
                  someone asks me when we can stop working on our
                  software.</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Now,
                  a few additional thoughts :</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="text-align:start;"><b>"10
                    years to build = 10 years to rebuild”</b></div>
                <div style="text-align:start;">I know
                  this was kind of a joke, and I know from experience
                  that it can sometimes feel true, but I want to add one
                  modifier here. It’s probably more like “20 person
                  years to build = 15 person years to rebuild.” An
                  “accidental SaaS” product like this often starts with
                  one engineer futzing around trying to solve a problem,
                  then a team accreting around them over the years like
                  barnacles on a shipwreck. Now you look at the team and
                  your brain extends the entire team back to the
                  beginning. A lot of that early work was either pretty
                  simple or it’s been rewritten, so it’s not quite that
                  bad. There’s also a ton of hidden business logic in
                  there, though, so even if you think you know what it’s
                  doing, you don’t, and you’ll need to rediscover it as
                  you go. How much has the team grown in the past few
                  years?</div>
                <div style="text-align:start;"><br>
                </div>
                <div style="text-align:start;"><b>What’s
                    the core value?&nbsp;</b></div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Over
                  the past ten years, the business and the software have
                  evolved, so it’s possible that you don’t need to
                  rebuild the current product, but rather to build a new
                  product that meets today’s needs. What’s that core
                  value? Can you carve that part off, offer it as a new
                  version, and migrate customers over? Then you don’t
                  have to try to figure out why it does that thing that
                  Bob wrote 9 1/2 years ago: you can build a new product
                  that does what customers need today. This is still a
                  major effort and will probably take a couple of years,
                  but if the business has changed significantly then it
                  might be a better option. Then you’re free to make
                  whatever tech choices you want while putting the
                  current product in maintenance mode.</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><b>Tech
                    choices</b></div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">I’m
                  with David: a productive team is more important than
                  the tech stack, but the ability to build a productive
                  team often depends upon using technology that
                  productive people want to use. As languages age, the
                  dynamics of the teams that work on them change. Mature
                  technologies tend to have more mature people working
                  with them, as the youngest (at heart) engineers move
                  on to the latest toys. As languages age out, you
                  generally go through stages where it gets harder to
                  find people who want to work in them full-time, then
                  you can only find outsourced companies that specialize
                  in them, then you have to bring someone out of
                  retirement to fix them. PHP is somewhere in the
                  “mature but not dying” stage right now, but if you
                  choose to build/rebuild a large product with it you
                  should think of it as a five-year commitment. Will you
                  be able to build the team you want for the next five
                  years?</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><b>A
                    story</b></div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Reed
                  Group wasn’t an accidental SaaS company, but it
                  definitely wasn’t a software company when I joined,
                  and the early years of the product were driven by some
                  very opinionated clients. When the product was about
                  five years old, a group of people who had been there
                  in the early years formed a competitor with the idea
                  that they could take what they’d learned at Reed Group
                  and build a new and better version of our enterprise
                  product in a year. They had a very light version live
                  in about a year, but their customers were unhappy with
                  all that was missing compared to our full-featured
                  version. It took them three years to create something
                  that was functionally comparable to the product they’d
                  left behind, and they’ve been developing full-speed
                  ever since to keep up with customer requests. So that
                  was approximately a 60% rebuild cost.</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                  <br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Jason
                  Cole</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">CEO</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><a href="https://www.daprimus.com" target="_blank" rel="nofollow noopener">Da Primus
                    Consulting</a></div>
                <span style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"></span><br>
                <span style="color:rgb(0,0,0);  font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;"></span><span></span>
              </div>
              <div><br>
                <blockquote>
                  <div>On Apr 26, 2022, at 10:23 AM, Sean Goodpasture
                    &lt;<a href="mailto:goofygrin@gmail.com" target="_blank" class="moz-txt-link-freetext" rel="nofollow noopener">goofygrin@gmail.com</a>&gt;
                    wrote:</div>
                  <br>
                  <div>
                    <div dir="ltr">David,&nbsp;
                      <div><br>
                      </div>
                      <div>You took the words out of my mouth - the
                        company is actually two - their current core
                        business and a software company.&nbsp; If they want
                        to be truly successful they need to run the
                        software as a product company and drive that
                        way.</div>
                      <div><br>
                      </div>
                      <div>There's lots of positives to spinning it as a
                        separate entity/subsidiary...<br>
                        <div><br>
                        </div>
                        <div>Sean</div>
                      </div>
                    </div>
                  </div>
                </blockquote>
              </div>
              <br>
            </div>
          </div>
        </blockquote>
      </div>
      
    </blockquote>
    <br>
    <pre class="moz-signature">-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a class="moz-txt-link-abbreviated" href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>
t: @rodandar</pre>
  
</div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204199615" aria-expanded="false" aria-controls="window-204199615"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204199615"><span id="likebutton204199615"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204199615, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204199615" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204199615">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4460907"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204199615"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204199615"><span id="likestats204199615"></span></div>
        </div>
      </div>
      
        <div id="window-204199615" class="collapse">
          <form class="form" id="form204199615" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204199615" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204199615">
            <input type="hidden" id="groupname204199615" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204199615" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204199615" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204199615" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204199615">
    <textarea id="editor204199615" name="editor204199615" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204199615"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204199615"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204199615" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204199615" value="html">
              

              <div id="bccme204199615" class="checkbox">
                <label for="bccme204199615">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204199615" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204199615"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204199615" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204199615" name="preview" onclick="editor.PreviewMarkdown(204199615,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204199615" name="return" onclick="editor.ReturnMarkdown(204199615)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204199615" data-toggle="collapse" data-target="#window-204199615"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204199615" onclick="editor.TogglePrivate('204199615', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204199615" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204199615">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204199615">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204199615" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204199615&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204199615" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204199615">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204199615">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204199615" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204199615&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204199615').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204199615').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204199615", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204199615').tooltip()
            $('#showHistory204199615').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204199615, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204199615, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5171"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Linda  Rolf
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 10:42am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5171"><span class="hidden-xs">#5171&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204200117">
        <div class="forcebreak" dir="auto"><meta http-equiv="Content-Type"><meta name="Generator"><div class="WordSection1"><p class="MsoNormal" style=""><span style="font-family:&amp;quot;  color:#404040;">Great thread with some excellent insights. The only contributions I can add are these –</span></p><p class="MsoNormal" style=""><span style="font-family:&amp;quot;  color:#404040;">&nbsp;</span></p><ol style="margin-top:0in;" type="1"><li class="MsoListParagraph" style="color:#404040;  margin-left:0in;"><span style="font-family:&amp;quot;">Having been at this for more than 30 years, I can 100% support the comments about time to rebuild. I learned early on that developers are an optimistic bunch when it comes to how long something will take to rewrite. One developer stated with absolute certainty that he could rewrite a core OS in 24 hours (it was 30 years ago when rolling your own was the norm). We soon after uncovered his substance abuse problem.</span></li><li class="MsoListParagraph" style="color:#404040;  margin-left:0in;"><span style="font-family:&amp;quot;">We all know that tech stacks will change over time. I also agree tech is less a factor than the team architecting and building. We rewrote an ASP/VB/SQL application quite a few years ago with .NET, the preferred tool at the time. Even with an excellent team of experienced developers, it took far longer than anticipated and left us saddled with .NET .</span></li></ol><p class="MsoNormal" style=""><span style="font-family:&amp;quot;  color:#404040;">&nbsp;</span></p><p class="MsoNormal" style=""><span style="font-family:&amp;quot;  color:#404040;">Linda Rolf</span></p><p class="MsoNormal" style=""><span style="font-family:&amp;quot;  color:#404040;">Quest Technology Group</span></p><p class="MsoNormal" style=""><span style="font-family:&amp;quot;  color:#404040;">www.quest-technology-group.com</span></p><p class="MsoNormal"><span style="font-family:&amp;quot;  color:#404040;">&nbsp;</span></p><div style=""><p class="MsoNormal"></p></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204200117" role="button" data-toggle="collapse" href="#quoted-204200117" aria-expanded="false" aria-controls="quoted-204200117"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204200117" class="collapse forcebreak">
            <div dir="auto"><b>From:</b> worldwide@ctolunches.groups.io &lt;worldwide@ctolunches.groups.io&gt; <b>On Behalf Of </b>Miles Cook<br><b>Sent:</b> Tuesday, April 26, 2022 1:14 PM<br><b>To:</b> Jason Cole &lt;jason@daprimus.com&gt;<br><b>Cc:</b> Sean Goodpasture &lt;goofygrin@gmail.com&gt;; worldwide &lt;worldwide@ctolunches.groups.io&gt;<br><b>Subject:</b> Re: [ctolunches] re-builds<p></p><p class="MsoNormal">&nbsp;</p><div><p class="MsoNormal" style="">Jason has some brilliant points, as well as the person that recommended using the strangler pattern. Used once to great effect to effectively rebuild critical parts of the plane in flight. Oh, and the new vode went to a new DDD folder, which could be ported over to the new API we would build.</p><div><p class="MsoNormal" style="">&nbsp;</p></div><div><p class="MsoNormal" style="">Its been interesting digesting these points. However, the tech stack? Tools are only as good as the tools using them! Recruitment or finding a good software house plays more of a part in consideration now more than ever.</p><div><p class="MsoNormal" style="">&nbsp;</p></div><div><p class="MsoNormal" style="">One thing I haven't seen - the why? I&nbsp; an think of a few reasons to rebuild a 10 year old tech stack but my worry would be, everything goes great, flawless migration then.... what did we achieve other than a load of spend? Would just be good to understand what isn't working or a problem on the horizon. If its something specific, that needs to be addressed first.</p></div><div><p class="MsoNormal" style="">&nbsp;</p></div><div><p class="MsoNormal" style="">Otherwise, no point in my trying to add to some fairly excellent observations in this thread.</p></div></div></div><p class="MsoNormal" style="">&nbsp;</p><div><div><p class="MsoNormal" style="">On Tue, 26 Apr 2022, 18:52 Jason Cole, &lt;<a href="mailto:jason@daprimus.com" rel="nofollow noopener" target="_blank">jason@daprimus.com</a>&gt; wrote:</p></div><blockquote><div><p class="MsoNormal" style="">First, this conversation has already given me some great quotes/war stories that I need to hear:</p><div><p class="MsoNormal" style="">&nbsp;</p></div><div><blockquote><p class="MsoNormal" style="">I've seen it done well maybe twice? But with a lot more failures (including a CTO telling me he could re-build the entire 15 year old codebase in .NET in three weeks—he did not succeed).</p></blockquote><div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">— Kendall Miller</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><blockquote><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">Software the runs live in front of customers?&nbsp; It's never "done" - so don't try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company folded and the IP got lost in the shareholder fight"</span></p></blockquote></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">— David Raistrick</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">Yeah, I’m definitely using that second one the next time someone asks me when we can stop working on our software.</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">Now, a few additional thoughts :</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><p class="MsoNormal" style=""><b><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">"10 years to build = 10 years to rebuild”</span></b></p></div><div><p class="MsoNormal" style="">I know this was kind of a joke, and I know from experience that it can sometimes feel true, but I want to add one modifier here. It’s probably more like “20 person years to build = 15 person years to rebuild.” An “accidental SaaS” product like this often starts with one engineer futzing around trying to solve a problem, then a team accreting around them over the years like barnacles on a shipwreck. Now you look at the team and your brain extends the entire team back to the beginning. A lot of that early work was either pretty simple or it’s been rewritten, so it’s not quite that bad. There’s also a ton of hidden business logic in there, though, so even if you think you know what it’s doing, you don’t, and you’ll need to rediscover it as you go. How much has the team grown in the past few years?</p></div><div><p class="MsoNormal" style="">&nbsp;</p></div><div><p class="MsoNormal" style=""><b>What’s the core value?&nbsp;</b></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">Over the past ten years, the business and the software have evolved, so it’s possible that you don’t need to rebuild the current product, but rather to build a new product that meets today’s needs. What’s that core value? Can you carve that part off, offer it as a new version, and migrate customers over? Then you don’t have to try to figure out why it does that thing that Bob wrote 9 1/2 years ago: you can build a new product that does what customers need today. This is still a major effort and will probably take a couple of years, but if the business has changed significantly then it might be a better option. Then you’re free to make whatever tech choices you want while putting the current product in maintenance mode.</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><p class="MsoNormal" style=""><b><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">Tech choices</span></b><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;"></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">I’m with David: a productive team is more important than the tech stack, but the ability to build a productive team often depends upon using technology that productive people want to use. As languages age, the dynamics of the teams that work on them change. Mature technologies tend to have more mature people working with them, as the youngest (at heart) engineers move on to the latest toys. As languages age out, you generally go through stages where it gets harder to find people who want to work in them full-time, then you can only find outsourced companies that specialize in them, then you have to bring someone out of retirement to fix them. PHP is somewhere in the “mature but not dying” stage right now, but if you choose to build/rebuild a large product with it you should think of it as a five-year commitment. Will you be able to build the team you want for the next five years?</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><p class="MsoNormal" style=""><b><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">A story</span></b><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;"></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">Reed Group wasn’t an accidental SaaS company, but it definitely wasn’t a software company when I joined, and the early years of the product were driven by some very opinionated clients. When the product was about five years old, a group of people who had been there in the early years formed a competitor with the idea that they could take what they’d learned at Reed Group and build a new and better version of our enterprise product in a year. They had a very light version live in about a year, but their customers were unhappy with all that was missing compared to our full-featured version. It took them three years to create something that was functionally comparable to the product they’d left behind, and they’ve been developing full-speed ever since to keep up with customer requests. So that was approximately a 60% rebuild cost.</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">&nbsp;</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">Jason Cole</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;">CEO</span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;"><a href="https://www.daprimus.com" target="_blank" rel="nofollow noopener">Da Primus Consulting</a></span></p></div><p class="MsoNormal" style=""><span style="font-size:9.0pt;  font-family:&amp;quot;  color:black;"><br></span></p></div><div><p class="MsoNormal" style=""><br><br></p><blockquote><div><p class="MsoNormal" style="">On Apr 26, 2022, at 10:23 AM, Sean Goodpasture &lt;<a href="mailto:goofygrin@gmail.com" target="_blank" rel="nofollow noopener">goofygrin@gmail.com</a>&gt; wrote:</p></div><p class="MsoNormal" style="">&nbsp;</p><div><div><p class="MsoNormal" style="">David,&nbsp;</p><div><p class="MsoNormal" style="">&nbsp;</p></div><div><p class="MsoNormal" style="">You took the words out of my mouth - the company is actually two - their current core business and a software company.&nbsp; If they want to be truly successful they need to run the software as a product company and drive that way.</p></div><div><p class="MsoNormal" style="">&nbsp;</p></div><div><p class="MsoNormal" style="">There's lots of positives to spinning it as a separate entity/subsidiary...</p><div><p class="MsoNormal" style="">&nbsp;</p></div><div><p class="MsoNormal" style="">Sean</p></div></div></div></div></blockquote></div><p class="MsoNormal" style="">&nbsp;</p></div></div></blockquote></div><div><p class="MsoNormal" style=""></p></div></div>
          </div>
          <script>
            $('#quoted-204200117').on('show.bs.collapse', function () {
              $('#qlabel-204200117').text("Hide quoted text");
            })
            $('#quoted-204200117').on('hide.bs.collapse', function () {
              $('#qlabel-204200117').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204200117" aria-expanded="false" aria-controls="window-204200117"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204200117"><span id="likebutton204200117"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204200117, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204200117" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204200117">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1406837"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204200117"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204200117"><span id="likestats204200117"></span></div>
        </div>
      </div>
      
        <div id="window-204200117" class="collapse">
          <form class="form" id="form204200117" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204200117" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204200117">
            <input type="hidden" id="groupname204200117" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204200117" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204200117" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204200117" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204200117">
    <textarea id="editor204200117" name="editor204200117" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204200117"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204200117"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204200117" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204200117" value="html">
              

              <div id="bccme204200117" class="checkbox">
                <label for="bccme204200117">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204200117" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204200117"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204200117" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204200117" name="preview" onclick="editor.PreviewMarkdown(204200117,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204200117" name="return" onclick="editor.ReturnMarkdown(204200117)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204200117" data-toggle="collapse" data-target="#window-204200117"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204200117" onclick="editor.TogglePrivate('204200117', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204200117" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204200117">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204200117">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204200117" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204200117&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204200117" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204200117">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204200117">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204200117" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204200117&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204200117').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204200117').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204200117", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204200117').tooltip()
            $('#showHistory204200117').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204200117, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204200117, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5172"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Naveed Ahmed
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 10:43am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5172"><span class="hidden-xs">#5172&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204200148">
        <div class="forcebreak" dir="auto"><div dir="ltr">I agree with you about all your concerns about rebuilds.<div><br></div><div>Just like a car, if the app hasn't been diligently well-maintained, it is time to get rid of it and buy a new one. Unlike a car though, it's not as simple. A rebuild for a 10 year-old system can take 1-2 years optimistically.&nbsp;</div><div><br></div><div>I don't think trying to make the new system work with the old one is a worthwhile exercise. It's the worst of both worlds. You are limited by most of whatever was wrong with the old system - then you're not really writing a new system, you're just updating it.</div><div><br></div><div>Despite the challenges and risks that you defined with a rewrite, you don't have a real choice. You will slowly start bleeding customers. You have to bite the&nbsp;bullet and start the rewrite.</div><div><br></div><div>I've found decent PHP developers very hard to find. The number of PHP developers is not small, but the number of qualified ones is.</div><div><br></div><div>I have rebuilt what was originally a PHP based system. I used Vue for the front-end and python for the backend, but today my recommendations for technologies are:</div><div>- React/Vue with Typescript for the frontend. I personally&nbsp;prefer Vue, but I realize react is more popular. I've found that paradoxically it's easier to hire Vue developers, they seem to self-select.</div><div>- Nest JS for the backend. This uses Typescript. NestJS is very highly opinionated and somewhat hard to get wrong and write spaghetti code like you can with PHP or Express.</div><div>- Postgres or MySQL for the backend. Both have their pros and cons. Postgres can get you more powerful queries easier and may be better for your domain.</div><div><br></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204200148" role="button" data-toggle="collapse" href="#quoted-204200148" aria-expanded="false" aria-controls="quoted-204200148"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204200148" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 10:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">
  

    
  
  <div>
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div>



  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204200148').on('show.bs.collapse', function () {
              $('#qlabel-204200148').text("Hide quoted text");
            })
            $('#quoted-204200148').on('hide.bs.collapse', function () {
              $('#qlabel-204200148').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204200148" aria-expanded="false" aria-controls="window-204200148"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204200148"><span id="likebutton204200148"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204200148, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204200148" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204200148">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4884680"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204200148"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204200148"><span id="likestats204200148"></span></div>
        </div>
      </div>
      
        <div id="window-204200148" class="collapse">
          <form class="form" id="form204200148" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204200148" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204200148">
            <input type="hidden" id="groupname204200148" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204200148" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204200148" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204200148" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204200148">
    <textarea id="editor204200148" name="editor204200148" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204200148"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204200148"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204200148" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204200148" value="html">
              

              <div id="bccme204200148" class="checkbox">
                <label for="bccme204200148">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204200148" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204200148"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204200148" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204200148" name="preview" onclick="editor.PreviewMarkdown(204200148,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204200148" name="return" onclick="editor.ReturnMarkdown(204200148)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204200148" data-toggle="collapse" data-target="#window-204200148"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204200148" onclick="editor.TogglePrivate('204200148', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204200148" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204200148">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204200148">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204200148" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204200148&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204200148" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204200148">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204200148">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204200148" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204200148&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204200148').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204200148').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204200148", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204200148').tooltip()
            $('#showHistory204200148').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204200148, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204200148, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5173"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Miles Cook
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 10:48am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5173"><span class="hidden-xs">#5173&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204200407">
        <div class="forcebreak" dir="auto"><div>Indeed! This thread caught my eye but I should read more... 😄<div><br></div><div>2 bread streams here: the health of the infrastructure to scale with more users, and the health of the code to build more features with confidence.&nbsp;</div><div><br></div><div>What would they place more importance on? It's a hard question because often truthfully, nobody has a crystal ball and wherever the revenue will come from is the answer.</div><div><br></div><div>Infrastructure is easy enough. MySql databases can just be made AWS's problem (or whoever you want to use). Instances&nbsp; an be moved from bare metal to scalable groups with sticky sessions or sessions in a dB.</div><div><br></div><div>Code? I'd do a review with them: what parts of the system are likely to be in demand for features. Then, with an experienced tech doing a sniff test, see what shape are they in. would it be useful if the business logic resided in a new place? If its discrete and seperable to the monolith, great. Find the seams, make an interface, build anew with a new feature.&nbsp; Loads of automated tests are a must.</div><div><br></div><div>I'm a big fan of risk aversion, rebuilding in chunks rather than big bang new build all at once. You get a much shorter feedback cycle for one!&nbsp;</div><div><br></div><div><br></div><div><br></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204200407" role="button" data-toggle="collapse" href="#quoted-204200407" aria-expanded="false" aria-controls="quoted-204200407"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204200407" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, 26 Apr 2022, 19:33 Dan Richards, &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">
  
    
  
  <div>
    Man, this group rocks sometimes, doesn't it?<br>
    <br>
    Great feedback from everyone, I really appreciate it.&nbsp;&nbsp; I framed
    this question because my role here is really as a trusted voice to
    the CEO and he knows I won't sell him a bunch of bullshit.&nbsp; He is
    NOT a software person, and knows that he doesn't know, which is why
    he has me. I mostly stay out of the the day-to-day process, so I
    don't have much vested in the team directly.&nbsp; So in this case my
    goal is simply to make sure he knows what kind of stuff he's about
    to step in on embarking on a project like this.&nbsp; As you all shared,
    it is much easier said than done!<br>
    <br>
    For those that speculated, the rationale driving this is the lure of
    larger clients with more demands, more data, etc. which obviously
    taxes and stresses the architecture, infrastructure, etc.<br>
    <br>
    Thanks everyone!<br>
    -Dan<br>
    <br>
    <div>On 4/26/22 1:13 PM, Miles Cook via
      <a href="http://groups.io" target="_blank" rel="nofollow noopener">groups.io</a> wrote:<br>
    </div>
    <blockquote>
      
      <div>Jason has some brilliant points, as well as the
        person that recommended using the strangler pattern. Used once
        to great effect to effectively rebuild critical parts of the
        plane in flight. Oh, and the new vode went to a new DDD folder,
        which could be ported over to the new API we would build.
        <div><br>
        </div>
        <div>Its been interesting digesting these points.
          However, the tech stack? Tools are only as good as the tools
          using them! Recruitment or finding a good software house plays
          more of a part in consideration now more than ever.
          <div><br>
          </div>
          <div>One thing I haven't seen - the why? I&nbsp; an
            think of a few reasons to rebuild a 10 year old tech stack
            but my worry would be, everything goes great, flawless
            migration then.... what did we achieve other than a load of
            spend? Would just be good to understand what isn't working
            or a problem on the horizon. If its something specific, that
            needs to be addressed first.</div>
          <div><br>
          </div>
          <div>Otherwise, no point in my trying to add to
            some fairly excellent observations in this thread.</div>
        </div>
      </div>
      <br>
      <div class="gmail_quote">
        <div dir="ltr" class="gmail_attr">On Tue, 26 Apr 2022, 18:52
          Jason Cole, &lt;<a href="mailto:jason@daprimus.com" target="_blank" rel="nofollow noopener">jason@daprimus.com</a>&gt;
          wrote:<br>
        </div>
        <blockquote class="gmail_quote">
          <div style="">First,
            this conversation has already given me some great quotes/war
            stories that I need to hear:
            <div><br>
            </div>
            <div>
              <blockquote>I've seen it done well maybe
                twice? But with a lot more failures (including a CTO
                telling me he could re-build the entire 15 year old
                codebase in .NET in three weeks—he did not succeed).</blockquote>
              <div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">—
                  Kendall Miller</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">
                  <blockquote>Software the runs live in
                    front of customers?&nbsp; It's never "done" - so don't
                    try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company
                    folded and the IP got lost in the shareholder fight"</blockquote>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">—
                  David Raistrick</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Yeah,
                  I’m definitely using that second one the next time
                  someone asks me when we can stop working on our
                  software.</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Now,
                  a few additional thoughts :</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="text-align:start;"><b>"10
                    years to build = 10 years to rebuild”</b></div>
                <div style="text-align:start;">I know
                  this was kind of a joke, and I know from experience
                  that it can sometimes feel true, but I want to add one
                  modifier here. It’s probably more like “20 person
                  years to build = 15 person years to rebuild.” An
                  “accidental SaaS” product like this often starts with
                  one engineer futzing around trying to solve a problem,
                  then a team accreting around them over the years like
                  barnacles on a shipwreck. Now you look at the team and
                  your brain extends the entire team back to the
                  beginning. A lot of that early work was either pretty
                  simple or it’s been rewritten, so it’s not quite that
                  bad. There’s also a ton of hidden business logic in
                  there, though, so even if you think you know what it’s
                  doing, you don’t, and you’ll need to rediscover it as
                  you go. How much has the team grown in the past few
                  years?</div>
                <div style="text-align:start;"><br>
                </div>
                <div style="text-align:start;"><b>What’s
                    the core value?&nbsp;</b></div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Over
                  the past ten years, the business and the software have
                  evolved, so it’s possible that you don’t need to
                  rebuild the current product, but rather to build a new
                  product that meets today’s needs. What’s that core
                  value? Can you carve that part off, offer it as a new
                  version, and migrate customers over? Then you don’t
                  have to try to figure out why it does that thing that
                  Bob wrote 9 1/2 years ago: you can build a new product
                  that does what customers need today. This is still a
                  major effort and will probably take a couple of years,
                  but if the business has changed significantly then it
                  might be a better option. Then you’re free to make
                  whatever tech choices you want while putting the
                  current product in maintenance mode.</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><b>Tech
                    choices</b></div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">I’m
                  with David: a productive team is more important than
                  the tech stack, but the ability to build a productive
                  team often depends upon using technology that
                  productive people want to use. As languages age, the
                  dynamics of the teams that work on them change. Mature
                  technologies tend to have more mature people working
                  with them, as the youngest (at heart) engineers move
                  on to the latest toys. As languages age out, you
                  generally go through stages where it gets harder to
                  find people who want to work in them full-time, then
                  you can only find outsourced companies that specialize
                  in them, then you have to bring someone out of
                  retirement to fix them. PHP is somewhere in the
                  “mature but not dying” stage right now, but if you
                  choose to build/rebuild a large product with it you
                  should think of it as a five-year commitment. Will you
                  be able to build the team you want for the next five
                  years?</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><b>A
                    story</b></div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Reed
                  Group wasn’t an accidental SaaS company, but it
                  definitely wasn’t a software company when I joined,
                  and the early years of the product were driven by some
                  very opinionated clients. When the product was about
                  five years old, a group of people who had been there
                  in the early years formed a competitor with the idea
                  that they could take what they’d learned at Reed Group
                  and build a new and better version of our enterprise
                  product in a year. They had a very light version live
                  in about a year, but their customers were unhappy with
                  all that was missing compared to our full-featured
                  version. It took them three years to create something
                  that was functionally comparable to the product they’d
                  left behind, and they’ve been developing full-speed
                  ever since to keep up with customer requests. So that
                  was approximately a 60% rebuild cost.</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><br>
                  <br>
                </div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">Jason
                  Cole</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);">CEO</div>
                <div style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"><a href="https://www.daprimus.com" target="_blank" rel="nofollow noopener">Da Primus
                    Consulting</a></div>
                <span style="font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;  color:rgb(0,0,0);"></span><br>
                <span style="color:rgb(0,0,0);  font-family:Helvetica;  font-size:12px;  font-style:normal;  font-weight:normal;  text-align:start;  text-decoration:none;"></span><span><img id="m_-6434885267114336451m_-4551483279191897856E54AEF94-77E9-4B5E-A5E5-E00C1382E5C6" class="myimg-responsive"></span>
              </div>
              <div><br>
                <blockquote>
                  <div>On Apr 26, 2022, at 10:23 AM, Sean Goodpasture
                    &lt;<a href="mailto:goofygrin@gmail.com" target="_blank" rel="nofollow noopener">goofygrin@gmail.com</a>&gt;
                    wrote:</div>
                  <br>
                  <div>
                    <div dir="ltr">David,&nbsp;
                      <div><br>
                      </div>
                      <div>You took the words out of my mouth - the
                        company is actually two - their current core
                        business and a software company.&nbsp; If they want
                        to be truly successful they need to run the
                        software as a product company and drive that
                        way.</div>
                      <div><br>
                      </div>
                      <div>There's lots of positives to spinning it as a
                        separate entity/subsidiary...<br>
                        <div><br>
                        </div>
                        <div>Sean</div>
                      </div>
                    </div>
                  </div>
                </blockquote>
              </div>
              <br>
            </div>
          </div>
        </blockquote>
      </div>
      
    </blockquote>
    <br>
    <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div>



  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204200407').on('show.bs.collapse', function () {
              $('#qlabel-204200407').text("Hide quoted text");
            })
            $('#quoted-204200407').on('hide.bs.collapse', function () {
              $('#qlabel-204200407').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204200407" aria-expanded="false" aria-controls="window-204200407"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204200407"><span id="likebutton204200407"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204200407, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204200407" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204200407">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4752701"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204200407"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204200407"><span id="likestats204200407"></span></div>
        </div>
      </div>
      
        <div id="window-204200407" class="collapse">
          <form class="form" id="form204200407" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204200407" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204200407">
            <input type="hidden" id="groupname204200407" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204200407" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204200407" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204200407" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204200407">
    <textarea id="editor204200407" name="editor204200407" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204200407"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204200407"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204200407" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204200407" value="html">
              

              <div id="bccme204200407" class="checkbox">
                <label for="bccme204200407">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204200407" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204200407"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204200407" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204200407" name="preview" onclick="editor.PreviewMarkdown(204200407,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204200407" name="return" onclick="editor.ReturnMarkdown(204200407)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204200407" data-toggle="collapse" data-target="#window-204200407"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204200407" onclick="editor.TogglePrivate('204200407', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204200407" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204200407">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204200407">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204200407" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204200407&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204200407" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204200407">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204200407">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204200407" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204200407&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204200407').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204200407').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204200407", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204200407').tooltip()
            $('#showHistory204200407').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204200407, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204200407, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5174"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Jacob Ablowitz
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 10:50am">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5174"><span class="hidden-xs">#5174&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204200525">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div dir="ltr">Agree with just about everything stated previously. Two addenda:<br><br>1) If your CEO decides to proceed with a strangler-pattern-style slow-but-steady rebuild via microservices, I'd recommend they focus recruiting&nbsp;upon&nbsp;<b>PHP+JS full-stack devs</b>. Given how it's virtually impossible to build a front end without JS nowadays, they shouldn't be much harder (if at all!) to find than PHP purists, and are relatively unlikely to object to a slow but steady move to full-stack JS or even better Typescript. JS is also pretty clearly a stack that is likely to survive long-term, and even most JS devs are game to learn TS as it is resume-enhancing to be able to do both.<br><br>2) The first thing I would do, if I were your CEO's CTO, would be to build a highly comprehensive suite of true end-to-end tests that thoroughly exercise all the key customer-facing workflows in the existing tool. Once this is complete and functioning, it allows you to swap out PHP components for the new&nbsp;microservices, whatever language they're built in, while still being able to confirm that <i>none of the core user-facing workflows in the system are broken</i>. This approach pays repeated dividends every single time there's a major upgrade to one of your underlying frameworks or third-party packages that could break stuff - you run your tests and quickly find out what's broken. This is one of the first things I did when I took over my current job - convincing my CEO that it was worth roughly 6 months of "minimal new feature development, bug-fixes only" to get those E2E tests done: major upgrades are now "an hour or two to a couple days max," like when we went straight from Ruby 2.4.2 and Rails 5 to Ruby 2.7.2 and Rails 6.1 in a day for a <i>very </i>complicated and multi-faceted backend api server monolith.</div><div dir="ltr"><br></div><div>Jacob</div><div dir="ltr"><br></div><div dir="ltr"><br></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204200525" role="button" data-toggle="collapse" href="#quoted-204200525" aria-expanded="false" aria-controls="quoted-204200525"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204200525" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 11:42 AM Linda  Rolf &lt;<a href="mailto:lrolf@quest-technology-group.com" target="_blank" rel="nofollow noopener">lrolf@quest-technology-group.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div lang="EN-US"><div><p class="MsoNormal" style=""><span style="font-family:Georgia,serif;  color:rgb(64,64,64);">Great thread with some excellent insights. The only contributions I can add are these –<u></u><u></u></span></p><p class="MsoNormal" style=""><span style="font-family:Georgia,serif;  color:rgb(64,64,64);"><u></u>&nbsp;<u></u></span></p><ol style="margin-top:0in;" type="1"><li style="color:rgb(64,64,64);  margin-left:0in;"><span style="font-family:Georgia,serif;">Having been at this for more than 30 years, I can 100% support the comments about time to rebuild. I learned early on that developers are an optimistic bunch when it comes to how long something will take to rewrite. One developer stated with absolute certainty that he could rewrite a core OS in 24 hours (it was 30 years ago when rolling your own was the norm). We soon after uncovered his substance abuse problem.<u></u><u></u></span></li><li style="color:rgb(64,64,64);  margin-left:0in;"><span style="font-family:Georgia,serif;">We all know that tech stacks will change over time. I also agree tech is less a factor than the team architecting and building. We rewrote an ASP/VB/SQL application quite a few years ago with .NET, the preferred tool at the time. Even with an excellent team of experienced developers, it took far longer than anticipated and left us saddled with .NET .<u></u><u></u></span></li></ol><p class="MsoNormal" style=""><span style="font-family:Georgia,serif;  color:rgb(64,64,64);"><u></u>&nbsp;<u></u></span></p><p class="MsoNormal" style=""><span style="font-family:Georgia,serif;  color:rgb(64,64,64);">Linda Rolf<u></u><u></u></span></p><p class="MsoNormal" style=""><span style="font-family:Georgia,serif;  color:rgb(64,64,64);">Quest Technology Group<u></u><u></u></span></p><p class="MsoNormal" style=""><span style="font-family:Georgia,serif;  color:rgb(64,64,64);"><a href="http://www.quest-technology-group.com" target="_blank" rel="nofollow noopener">www.quest-technology-group.com</a><u></u><u></u></span></p><p class="MsoNormal"><span style="font-family:Georgia,serif;  color:rgb(64,64,64);"><u></u>&nbsp;<u></u></span></p><div style=""><p class="MsoNormal"><b>From:</b> <a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a> &lt;<a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a>&gt; <b>On Behalf Of </b>Miles Cook<br><b>Sent:</b> Tuesday, April 26, 2022 1:14 PM<br><b>To:</b> Jason Cole &lt;<a href="mailto:jason@daprimus.com" target="_blank" rel="nofollow noopener">jason@daprimus.com</a>&gt;<br><b>Cc:</b> Sean Goodpasture &lt;<a href="mailto:goofygrin@gmail.com" target="_blank" rel="nofollow noopener">goofygrin@gmail.com</a>&gt;; worldwide &lt;<a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a>&gt;<br><b>Subject:</b> Re: [ctolunches] re-builds<u></u><u></u></p></div><p class="MsoNormal"><u></u>&nbsp;<u></u></p><div><p class="MsoNormal" style="">Jason has some brilliant points, as well as the person that recommended using the strangler pattern. Used once to great effect to effectively rebuild critical parts of the plane in flight. Oh, and the new vode went to a new DDD folder, which could be ported over to the new API we would build.<u></u><u></u></p><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><p class="MsoNormal" style="">Its been interesting digesting these points. However, the tech stack? Tools are only as good as the tools using them! Recruitment or finding a good software house plays more of a part in consideration now more than ever.<u></u><u></u></p><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><p class="MsoNormal" style="">One thing I haven't seen - the why? I&nbsp; an think of a few reasons to rebuild a 10 year old tech stack but my worry would be, everything goes great, flawless migration then.... what did we achieve other than a load of spend? Would just be good to understand what isn't working or a problem on the horizon. If its something specific, that needs to be addressed first.<u></u><u></u></p></div><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><p class="MsoNormal" style="">Otherwise, no point in my trying to add to some fairly excellent observations in this thread.<u></u><u></u></p></div></div></div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p><div><div><p class="MsoNormal" style="">On Tue, 26 Apr 2022, 18:52 Jason Cole, &lt;<a href="mailto:jason@daprimus.com" target="_blank" rel="nofollow noopener">jason@daprimus.com</a>&gt; wrote:<u></u><u></u></p></div><blockquote><div><p class="MsoNormal" style="">First, this conversation has already given me some great quotes/war stories that I need to hear:<u></u><u></u></p><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><blockquote><p class="MsoNormal" style="">I've seen it done well maybe twice? But with a lot more failures (including a CTO telling me he could re-build the entire 15 year old codebase in .NET in three weeks—he did not succeed).<u></u><u></u></p></blockquote><div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">— Kendall Miller<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><blockquote><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">Software the runs live in front of customers?&nbsp; It's never "done" - so don't try to put "done" on a roadmap.&nbsp; &nbsp;"Done" is "company folded and the IP got lost in the shareholder fight"<u></u><u></u></span></p></blockquote></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">— David Raistrick<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">Yeah, I’m definitely using that second one the next time someone asks me when we can stop working on our software.<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">Now, a few additional thoughts :<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><p class="MsoNormal" style=""><b><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">"10 years to build = 10 years to rebuild”</span></b><u></u><u></u></p></div><div><p class="MsoNormal" style="">I know this was kind of a joke, and I know from experience that it can sometimes feel true, but I want to add one modifier here. It’s probably more like “20 person years to build = 15 person years to rebuild.” An “accidental SaaS” product like this often starts with one engineer futzing around trying to solve a problem, then a team accreting around them over the years like barnacles on a shipwreck. Now you look at the team and your brain extends the entire team back to the beginning. A lot of that early work was either pretty simple or it’s been rewritten, so it’s not quite that bad. There’s also a ton of hidden business logic in there, though, so even if you think you know what it’s doing, you don’t, and you’ll need to rediscover it as you go. How much has the team grown in the past few years?<u></u><u></u></p></div><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><p class="MsoNormal" style=""><b>What’s the core value?&nbsp;</b><u></u><u></u></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">Over the past ten years, the business and the software have evolved, so it’s possible that you don’t need to rebuild the current product, but rather to build a new product that meets today’s needs. What’s that core value? Can you carve that part off, offer it as a new version, and migrate customers over? Then you don’t have to try to figure out why it does that thing that Bob wrote 9 1/2 years ago: you can build a new product that does what customers need today. This is still a major effort and will probably take a couple of years, but if the business has changed significantly then it might be a better option. Then you’re free to make whatever tech choices you want while putting the current product in maintenance mode.<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><p class="MsoNormal" style=""><b><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">Tech choices</span></b><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">I’m with David: a productive team is more important than the tech stack, but the ability to build a productive team often depends upon using technology that productive people want to use. As languages age, the dynamics of the teams that work on them change. Mature technologies tend to have more mature people working with them, as the youngest (at heart) engineers move on to the latest toys. As languages age out, you generally go through stages where it gets harder to find people who want to work in them full-time, then you can only find outsourced companies that specialize in them, then you have to bring someone out of retirement to fix them. PHP is somewhere in the “mature but not dying” stage right now, but if you choose to build/rebuild a large product with it you should think of it as a five-year commitment. Will you be able to build the team you want for the next five years?<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><p class="MsoNormal" style=""><b><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">A story</span></b><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">Reed Group wasn’t an accidental SaaS company, but it definitely wasn’t a software company when I joined, and the early years of the product were driven by some very opinionated clients. When the product was about five years old, a group of people who had been there in the early years formed a competitor with the idea that they could take what they’d learned at Reed Group and build a new and better version of our enterprise product in a year. They had a very light version live in about a year, but their customers were unhappy with all that was missing compared to our full-featured version. It took them three years to create something that was functionally comparable to the product they’d left behind, and they’ve been developing full-speed ever since to keep up with customer requests. So that was approximately a 60% rebuild cost.<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><u></u>&nbsp;<u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">Jason Cole<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;">CEO<u></u><u></u></span></p></div><div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><a href="https://www.daprimus.com" target="_blank" rel="nofollow noopener">Da Primus Consulting</a><u></u><u></u></span></p></div><p class="MsoNormal" style=""><span style="font-size:9pt;  font-family:Helvetica,sans-serif;  color:black;"><br></span><img width="32" height="32" style="width: 0.3333in;" id="gmail-m_-5667096009074411184gmail-m_4163022824869129834_x0000_i1027" class="myimg-responsive"><u></u><u></u></p></div><div><p class="MsoNormal" style=""><br><br><u></u><u></u></p><blockquote><div><p class="MsoNormal" style="">On Apr 26, 2022, at 10:23 AM, Sean Goodpasture &lt;<a href="mailto:goofygrin@gmail.com" target="_blank" rel="nofollow noopener">goofygrin@gmail.com</a>&gt; wrote:<u></u><u></u></p></div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p><div><div><p class="MsoNormal" style="">David,&nbsp;<u></u><u></u></p><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><p class="MsoNormal" style="">You took the words out of my mouth - the company is actually two - their current core business and a software company.&nbsp; If they want to be truly successful they need to run the software as a product company and drive that way.<u></u><u></u></p></div><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><p class="MsoNormal" style="">There's lots of positives to spinning it as a separate entity/subsidiary...<u></u><u></u></p><div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div><div><p class="MsoNormal" style="">Sean<u></u><u></u></p></div></div></div></div></blockquote></div><p class="MsoNormal" style=""><u></u>&nbsp;<u></u></p></div></div></blockquote></div><div><p class="MsoNormal" style=""><u></u></p></div></div></div>


  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204200525').on('show.bs.collapse', function () {
              $('#qlabel-204200525').text("Hide quoted text");
            })
            $('#quoted-204200525').on('hide.bs.collapse', function () {
              $('#qlabel-204200525').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204200525" aria-expanded="false" aria-controls="window-204200525"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204200525"><span id="likebutton204200525"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204200525, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204200525" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204200525">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388202"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204200525"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204200525"><span id="likestats204200525"></span></div>
        </div>
      </div>
      
        <div id="window-204200525" class="collapse">
          <form class="form" id="form204200525" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204200525" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204200525">
            <input type="hidden" id="groupname204200525" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204200525" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204200525" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204200525" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204200525">
    <textarea id="editor204200525" name="editor204200525" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204200525"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204200525"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204200525" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204200525" value="html">
              

              <div id="bccme204200525" class="checkbox">
                <label for="bccme204200525">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204200525" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204200525"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204200525" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204200525" name="preview" onclick="editor.PreviewMarkdown(204200525,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204200525" name="return" onclick="editor.ReturnMarkdown(204200525)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204200525" data-toggle="collapse" data-target="#window-204200525"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204200525" onclick="editor.TogglePrivate('204200525', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204200525" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204200525">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204200525">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204200525" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204200525&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204200525" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204200525">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204200525">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204200525" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204200525&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204200525').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204200525').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204200525", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204200525').tooltip()
            $('#showHistory204200525').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204200525, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204200525, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5178"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Josiah Haswell
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 12:29pm">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5178"><span class="hidden-xs">#5178&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204205594">
        <div class="forcebreak" dir="auto">I worked on HP OpenView over 10 years ago which was a complex, enterprise network monitoring system with thousands of customers.&nbsp; The system had been in continuous development since the 80's, but it had reached the point where adding any new functionality whatsoever would break existing functionality or simply take years to implement. HP was faced with a choice: retire the product or rewrite it.&nbsp; They eventually gave the team 1 year (this was waterfall, mind you, so that was 1 release) to release the core SNMP product.&nbsp; We managed it and rewrite paid off and continues to be a leader in the space, but here's what I learned.<br><br>1. I absolutely agree with David here. Think about the core challenges that your team faces in the existing product: are they related to specifics of your existing tech stack?&nbsp; If so, consider the most similar tech stack to yours that resolves those specific issues.&nbsp; Any new, radically different technology stack is likely to slow you down dramatically and result in a huge amount of technical debt that may make the product worse. I disagree that PHP/Laravel are not modern or effective, but there is a high cost to moving away that you will certainly pay. The language syntax differences may be whatever (although they are&nbsp;<em>substantial</em> if you change paradigms such as OO-&gt;functional or event-driven/async), but the entire ecosystem is different and that is non-trivial.<br><br>2. Microservices are a solution to scalability problems, not complexity problems.&nbsp; Software-defined networking is much simpler than physical networking, but it is still not an easy skillset to teach a team that does not already have it, it's difficult to hire for, and absolutely will increase both the overall complexity of your application and the security-vulnerability surface area of it. If it doesn't solve an existing problem, I would think carefully as to whether you need it as microservice architectures are much harder to build, secure, and maintain than monolithic architectures.<br><br>3. The strangler fig pattern is tricky to get right in practice and might saddle you with the same structural problems you already have. It might be suitable if the technical debt has been built around a sound core foundation, but I would consider an alternative such as putting the existing application into maintenance mode and rebuilding from a prioritized list of features.&nbsp;&nbsp;<br><br>4. If you are planning on changing tech stacks, try having your senior engineering team build out some non-trivial strawmen applications to stress-test the platform.&nbsp; Have them implement some microservices.&nbsp; Everything is likely to change from runtime characteristics to build tools to deployment models. Benchmark the time to complete the same task on each platform and extrapolate from that.&nbsp; This will help distinguish the hype from the reality that you will be working in.<br><br>HTH!<br><br>Josiah</div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204205594" aria-expanded="false" aria-controls="window-204205594"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204205594"><span id="likebutton204205594"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204205594, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204205594" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204205594">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1681689"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204205594"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204205594"><span id="likestats204205594"></span></div>
        </div>
      </div>
      
        <div id="window-204205594" class="collapse">
          <form class="form" id="form204205594" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204205594" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204205594">
            <input type="hidden" id="groupname204205594" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204205594" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204205594" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204205594" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204205594">
    <textarea id="editor204205594" name="editor204205594" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204205594"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204205594"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204205594" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204205594" value="html">
              

              <div id="bccme204205594" class="checkbox">
                <label for="bccme204205594">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204205594" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204205594"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204205594" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204205594" name="preview" onclick="editor.PreviewMarkdown(204205594,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204205594" name="return" onclick="editor.ReturnMarkdown(204205594)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204205594" data-toggle="collapse" data-target="#window-204205594"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204205594" onclick="editor.TogglePrivate('204205594', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204205594" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204205594">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204205594">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204205594" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204205594&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204205594" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204205594">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204205594">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204205594" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204205594&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204205594').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204205594').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204205594", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204205594').tooltip()
            $('#showHistory204205594').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204205594, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204205594, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5179"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    david raistrick
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 12:39pm">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5179"><span class="hidden-xs">#5179&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204206132">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div dir="ltr">yes!<div><br></div><div>thanks for 2) - that's a horse I've given up on trying to convince people away from (mostly).&nbsp; &nbsp;service are great.&nbsp; hundreds of services are a problem that creates a large org full of hard-to-fill roles.&nbsp; (sometimes that is what you want....)<br><br></div><div>on 4) - take those straw men through the entire lifecycle.&nbsp; build them into your daily workflow, get them running in production.&nbsp; don't let them stop at "this was fun, and it runs great on local!" - the entire pipeline and lifecycle are important parts to learn during that.</div><div><br></div><div><br></div><div><br></div></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204206132" role="button" data-toggle="collapse" href="#quoted-204206132" aria-expanded="false" aria-controls="quoted-204206132"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204206132" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 3:29 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" rel="nofollow noopener" target="_blank">josiah@sunshower.io</a>&gt; wrote:<br></div><blockquote class="gmail_quote">I worked on HP OpenView over 10 years ago which was a complex, enterprise network monitoring system with thousands of customers.&nbsp; The system had been in continuous development since the 80's, but it had reached the point where adding any new functionality whatsoever would break existing functionality or simply take years to implement. HP was faced with a choice: retire the product or rewrite it.&nbsp; They eventually gave the team 1 year (this was waterfall, mind you, so that was 1 release) to release the core SNMP product.&nbsp; We managed it and rewrite paid off and continues to be a leader in the space, but here's what I learned.<br><br>1. I absolutely agree with David here. Think about the core challenges that your team faces in the existing product: are they related to specifics of your existing tech stack?&nbsp; If so, consider the most similar tech stack to yours that resolves those specific issues.&nbsp; Any new, radically different technology stack is likely to slow you down dramatically and result in a huge amount of technical debt that may make the product worse. I disagree that PHP/Laravel are not modern or effective, but there is a high cost to moving away that you will certainly pay. The language syntax differences may be whatever (although they are&nbsp;<em>substantial</em> if you change paradigms such as OO-&gt;functional or event-driven/async), but the entire ecosystem is different and that is non-trivial.<br><br>2. Microservices are a solution to scalability problems, not complexity problems.&nbsp; Software-defined networking is much simpler than physical networking, but it is still not an easy skillset to teach a team that does not already have it, it's difficult to hire for, and absolutely will increase both the overall complexity of your application and the security-vulnerability surface area of it. If it doesn't solve an existing problem, I would think carefully as to whether you need it as microservice architectures are much harder to build, secure, and maintain than monolithic architectures.<br><br>3. The strangler fig pattern is tricky to get right in practice and might saddle you with the same structural problems you already have. It might be suitable if the technical debt has been built around a sound core foundation, but I would consider an alternative such as putting the existing application into maintenance mode and rebuilding from a prioritized list of features.&nbsp;&nbsp;<br><br>4. If you are planning on changing tech stacks, try having your senior engineering team build out some non-trivial strawmen applications to stress-test the platform.&nbsp; Have them implement some microservices.&nbsp; Everything is likely to change from runtime characteristics to build tools to deployment models. Benchmark the time to complete the same task on each platform and extrapolate from that.&nbsp; This will help distinguish the hype from the reality that you will be working in.<br><br>HTH!<br><br>Josiah


  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204206132').on('show.bs.collapse', function () {
              $('#qlabel-204206132').text("Hide quoted text");
            })
            $('#quoted-204206132').on('hide.bs.collapse', function () {
              $('#qlabel-204206132').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204206132" aria-expanded="false" aria-controls="window-204206132"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204206132"><span id="likebutton204206132"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204206132, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204206132" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204206132">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:231388"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204206132"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204206132"><span id="likestats204206132"></span></div>
        </div>
      </div>
      
        <div id="window-204206132" class="collapse">
          <form class="form" id="form204206132" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204206132" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204206132">
            <input type="hidden" id="groupname204206132" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204206132" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204206132" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204206132" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204206132">
    <textarea id="editor204206132" name="editor204206132" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204206132"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204206132"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204206132" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204206132" value="html">
              

              <div id="bccme204206132" class="checkbox">
                <label for="bccme204206132">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204206132" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204206132"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204206132" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204206132" name="preview" onclick="editor.PreviewMarkdown(204206132,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204206132" name="return" onclick="editor.ReturnMarkdown(204206132)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204206132" data-toggle="collapse" data-target="#window-204206132"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204206132" onclick="editor.TogglePrivate('204206132', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204206132" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204206132">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204206132">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204206132" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204206132&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204206132" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204206132">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204206132">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204206132" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204206132&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204206132').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204206132').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204206132", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204206132').tooltip()
            $('#showHistory204206132').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204206132, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204206132, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5182"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Ryan Vice
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 1:11pm">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5182"><span class="hidden-xs">#5182&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204207800">
        <div class="forcebreak" dir="auto"><div>
<div>I’m partner in a agency and we’ve helped with rewrites. Lots of great points. My thoughts:<br></div>
<ol type="1">
<li>The current code is most likely your best documentation of the system and that’s the hardest thing about rewriting old systems</li>
<li>Second hardest is political, make sure you can get wins early. We usually try and put an API over the old system and then update UI first as like for like ish. This allows giving stakeholders some new shinny in the short term. Then use things like strangler for BE but I’d look for opportunities to refactor and reuse the existing business logic especially for the complex high value pieces</li>
<li>+1 for full stack JavaScript. It allows you to do more with smaller teams and you can look at doing mobile down the road, etc… provides additional strategic value to pitch to stakeholders</li>
</ol>
</div>
<div><br>
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td>
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td width="150"><span class="sc-kgAjT cuzzPp" style=" display: block;"><img src="https://vicesoftware.com/wp-content/uploads/2021/11/ryan-vice.png" width="130" class="sc-cHGsZl bHiaRe myimg-responsive" style="max-width: 130px;"></span></td>
<td>
<h3 class="sc-fBuWsC eeihxG" style=" font-size: 18px;   color: rgb(0, 0, 0);"><span>Ryan</span><span>&nbsp;</span><span>Vice</span></h3>
<p class="sc-fMiknA bxZCMx" style=" color: rgb(0, 0, 0);   font-size: 14px;"><span>CEO</span></p>
<p class="sc-dVhcbM fghLuF" style=" font-weight: 500;   color: rgb(0, 0, 0);   font-size: 14px;"><span>Vice Software, LLC</span></p>
</td>
<td width="30">
<div style="width: 30px;"></div>
</td>
<td width="1" class="sc-jhAzac hmXDXQ"></td>
<td width="30">
<div style="width: 30px;"></div>
</td>
<td>
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td width="30">
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td><span class="sc-jlyJG bbyJzT" style="display: block;   background-color: rgb(240, 131, 0);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/phone-icon-2x.png" width="13" class="sc-iRbamj blSEcj myimg-responsive" style="display: block;   background-color: rgb(240, 131, 0);"></span></td>
</tr>
</tbody>
</table>
</td>
<td><a href="tel:1%20(855)%20349-2248" class="sc-gipzik iyhjGb" rel="nofollow noopener" target="_blank"><span>1 (855) 349-2248</span></a> | <a href="tel:1%20(512)%20788-1126" class="sc-gipzik iyhjGb" rel="nofollow noopener" target="_blank"><span>1 (512) 788-1126</span></a></td>
</tr>
<tr>
<td width="30">
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td><span class="sc-jlyJG bbyJzT" style="display: block;   background-color: rgb(240, 131, 0);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/email-icon-2x.png" width="13" class="sc-iRbamj blSEcj myimg-responsive" style="display: block;   background-color: rgb(240, 131, 0);"></span></td>
</tr>
</tbody>
</table>
</td>
<td><a href="mailto:ryan@vicesoftware.com" class="sc-gipzik iyhjGb" rel="nofollow noopener" target="_blank"><span>ryan@vicesoftware.com</span></a></td>
</tr>
<tr>
<td width="30">
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td><span class="sc-jlyJG bbyJzT" style="display: block;   background-color: rgb(240, 131, 0);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/link-icon-2x.png" width="13" class="sc-iRbamj blSEcj myimg-responsive" style="display: block;   background-color: rgb(240, 131, 0);"></span></td>
</tr>
</tbody>
</table>
</td>
<td><a href="//www.vicesoftware.com" class="sc-gipzik iyhjGb" rel="nofollow noopener" target="_blank"><span>www.vicesoftware.com</span></a></td>
</tr>
<tr>
<td width="30">
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td><span class="sc-jlyJG bbyJzT" style="display: block;   background-color: rgb(240, 131, 0);"><img src="https://cdn2.hubspot.net/hubfs/53/tools/email-signature-generator/icons/address-icon-2x.png" width="13" class="sc-iRbamj blSEcj myimg-responsive" style="display: block;   background-color: rgb(240, 131, 0);"></span></td>
</tr>
</tbody>
</table>
</td>
<td><span class="sc-csuQGl CQhxV" style="font-size: 12px;   color: rgb(0, 0, 0);"><span>10614 Sans Souci PL, Austin, TX 78759</span></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td height="30"></td>
</tr>
<tr>
<td height="1" class="sc-jhAzac hmXDXQ"></td>
</tr>
<tr>
<td height="30"></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td>
<table class="sc-gPEVay eQYmiW">
<tbody>
<tr>
<td></td>
<td></td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><span style="display: inline;   text-align: left;"><a target="_blank" href="//" class="sc-fAjcbJ byigni" rel="nofollow noopener"><img src="https://vicesoftware.com/wp-content/uploads/2022/01/FTC-Badge-Square-Blue-2022.png" class="sc-caSCKo jjNSwx myimg-responsive" style="text-decoration: none;   max-width: 100px;"></a></span> <span style="display: inline;   text-align: left;"><a target="_blank" href="//" class="sc-fAjcbJ byigni" rel="nofollow noopener"><img src="https://vicesoftware.com/wp-content/uploads/2022/01/mvp.png" class="sc-caSCKo jjNSwx myimg-responsive" style="text-decoration: none;"></a></span></td>
</tr>
<tr>
<td height="30"></td>
</tr>
</tbody>
</table>
</div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204207800" role="button" data-toggle="collapse" href="#quoted-204207800" aria-expanded="false" aria-controls="quoted-204207800"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204207800" class="collapse forcebreak">
            <div dir="auto"><div>On Apr 26, 2022, 12:16 PM -0500, M david raistrick &lt;keen@icantclick.org&gt;, wrote:<br>
<blockquote><br>
<div>developers</div>
</blockquote>
</div>

</div>
          </div>
          <script>
            $('#quoted-204207800').on('show.bs.collapse', function () {
              $('#qlabel-204207800').text("Hide quoted text");
            })
            $('#quoted-204207800').on('hide.bs.collapse', function () {
              $('#qlabel-204207800').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204207800" aria-expanded="false" aria-controls="window-204207800"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204207800"><span id="likebutton204207800"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204207800, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204207800" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204207800">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1443309"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204207800"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204207800"><span id="likestats204207800"></span></div>
        </div>
      </div>
      
        <div id="window-204207800" class="collapse">
          <form class="form" id="form204207800" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,0,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204207800" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204207800">
            <input type="hidden" id="groupname204207800" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204207800" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204207800" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204207800" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204207800">
    <textarea id="editor204207800" name="editor204207800" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204207800"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204207800"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204207800" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204207800" value="html">
              

              <div id="bccme204207800" class="checkbox">
                <label for="bccme204207800">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204207800" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204207800"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204207800" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204207800" name="preview" onclick="editor.PreviewMarkdown(204207800,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204207800" name="return" onclick="editor.ReturnMarkdown(204207800)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204207800" data-toggle="collapse" data-target="#window-204207800"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204207800" onclick="editor.TogglePrivate('204207800', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204207800" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204207800">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204207800">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204207800" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204207800&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204207800" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204207800">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204207800">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204207800" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204207800&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204207800').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204207800').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204207800", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204207800').tooltip()
            $('#showHistory204207800').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204207800, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204207800, false)
      </script>
    
    
  </tr>



</tbody></table>

<form class="form" method="POST" action="https://ctolunches.groups.io/g/worldwide/editmessage">
  
    <input type="hidden" name="csrf" value="5276883099450123193">
  
  <input type="hidden" name="mid" id="mid" value="0">
  <input type="hidden" name="action_type" id="action_type" value="delete">

  <!-- Verify Remove Modal -->
  <div class="modal fade" id="deleteMessageModal" tabindex="-1" role="dialog" aria-labelledby="deleteMessageModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
          <h4 class="modal-title" id="deleteMessageModalLabel">Verify Delete</h4>
        </div>
        <div class="modal-body">
        Are you sure you wish to delete this message from the message archives of worldwide@ctolunches.groups.io? <strong>This cannot be undone.</strong>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
          <button class="btn btn-danger btn-sm" name="delmessage" value="1"><i class="fa fa-trash-alt"></i> Yes</button>
        </div>
      </div>
    </div>
  </div>
</form>

  <form class="form" method="POST" action="https://ctolunches.groups.io/g/worldwide/repostmessage">
    
      <input type="hidden" name="csrf" value="5276883099450123193">
    
    <input type="hidden" name="mid" id="repostmid" value="0">
    <input type="hidden" name="r" value="https://ctolunches.groups.io/g/worldwide/messages">

    <!-- Verify Repost Modal -->
    <div class="modal fade" id="repostMessageModal" tabindex="-1" role="dialog" aria-labelledby="repostMessageModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title" id="repostMessageModalLabel">Verify Repost</h4>
          </div>
          <div class="modal-body">
          Are you sure you wish to repost this message?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
            <button class="btn btn-danger btn-sm" name="delmessage" value="1"><i class="fa fa-retweet"></i> Yes</button>
          </div>
        </div>
      </div>
    </div>
  </form>


  <form class="form" id="reportform" method="POST" action="https://ctolunches.groups.io/g/worldwide/report">
    
      <input type="hidden" name="csrf" value="5276883099450123193">
    
    <input type="hidden" name="mid" id="reportmid" value="0">

    <!-- Report Message Modal -->
    <div class="modal fade" id="reportMessageModal" tabindex="-1" role="dialog" aria-labelledby="reportMessageModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title" id="reportMessageModalLabel">Report Message</h4>
          </div>
          <div class="modal-body">
            <label for="reason">Reason</label>
            <textarea id="reason" name="reason" class="form-control" rows="5"></textarea>

            <div class="radio">
              <label>
                <input type="radio" name="reportto" value="mods" checked="">Report to Moderators
              </label>
              <span class="help-block">I think this message isn't appropriate for our group. The Group moderators are responsible for maintaining their community and can address these issues.</span>
              <label>
                <input type="radio" name="reportto" value="support">Report to Groups.io Support
              </label>
              <span class="help-block">I think this violates the Terms of Service. This includes: harm to minors, violence or threats, harassment or privacy invasion, impersonation or misrepresentation, fraud or phishing.</span>
            </div>

            <p></p><center><strong>Note:</strong> Your email address is included with the abuse report.</center><p></p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
            <button type="submit" class="btn btn-danger btn-sm" name="report" value="1"><i class="fa fa-flag"></i> Report</button>
          </div>
        </div>
      </div>
    </div>
  </form>

  <script>
  $('#reportMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#reportmid').val(msgId);
  });
  $(function() {
    $('#reportform').on('submit', function(event){
        event.preventDefault(); 
        $('#reportMessageModal').modal('hide');
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            success: function(html) {
              createAlert("Your report has been sent", true);
            }
        });
        return false; 
    });
  });
  </script>


<form class="form" method="POST" action="https://ctolunches.groups.io/g/worldwide/editmessage">
  
    <input type="hidden" name="csrf" value="5276883099450123193">
  
  <input type="hidden" name="mid" id="splitmid" value="0">
  <input type="hidden" name="action_type" id="action_type" value="split">
  <input type="hidden" name="r" value="https://ctolunches.groups.io/g/worldwide/topic/90710568">
  <!-- Verify Split Modal -->
  <div class="modal fade" id="splitMessageModal" tabindex="-1" role="dialog" aria-labelledby="splitMessageModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
          <h4 class="modal-title" id="splitMessageModalLabel">Split Topic</h4>
        </div>
        <div class="modal-body">
        <p>The new topic will begin with this message. Subject of the new topic:</p>
                <input name="subject" class="form-control" size="20" type="text" spellcheck="true">
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
          <button class="btn btn-danger btn-sm" name="delmessage" value="1"><i class="fa fa-trash-alt"></i> Split Topic</button>
        </div>
      </div>
    </div>
  </div>
</form>

<div class="row">
  <div class="col-xs-12">


  
    <div class="pull-right">
      <table>
        <tbody><tr>
          <td>
						
							1 - 20 of 34
						
          </td>
          <td>
            &nbsp;
          </td>
          <td>
            <ul class="pagination">
              
                <li class="disabled"><a href="#"><i class="fa fa-chevron-left"><span class="sr-only">previous page</span></i></a></li>
              
              
                
                  <li class="disabled"><a class="currentpage" href="#">1</a></li>
                
              
                
                  <li><a href="https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p=Created%2C%2C%2C20%2C1%2C20%2C0&amp;jump=1" rel="nofollow">2</a></li>
                
              
              
                <li><a href="https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p=Created%2C%2C%2C20%2C1%2C20%2C0&amp;next=1"><i class="fa fa-chevron-right"><span class="sr-only">next page</span></i></a></li>
              
            </ul>
          </td>
        </tr>
      </tbody></table>
    </div>
  


<a href="https://ctolunches.groups.io/g/worldwide/topic/90797773?p=,,,20,0,0,0::,,,0,0,0,90797773" class="btn btn-default btn-sm"><i class="fa fa-arrow-left"></i><span class="hidden-xs">  Previous Topic</span></a>
<a href="https://ctolunches.groups.io/g/worldwide/topic/90839830?p=,,,20,0,0,0::,,,0,0,0,90839830" class="btn btn-default btn-sm"><i class="fa fa-arrow-right"></i><span class="hidden-xs"> Next Topic</span></a>

  </div>
</div>

<script>
  $('#deleteMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#mid').val(msgId);
  });
  $('#splitMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#splitmid').val(msgId);
  });
  $('#repostMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#repostmid').val(msgId);
  });
  $('[id^=cancel]').on('click', function() {
      msg_num = $(this).attr('id').split("-")[1]
      $("#window-"+msg_num).collapse('hide')
  });

  if (location.hash) {
    location.href = location.hash;
  }

  $(".modal").on('shown.bs.modal', function () {
      $(this).find("input:visible:first").focus();
  });
  console.log("JSVERSION:", jsBundleVersion());
$("[data-toggle='tooltip']").tooltip();
</script>

<script>

  var nextPage = ""
  var ele = "#records div.test";
  var runawayCounter = 0;
  gioDestroy(function(event) {
    console.log("in gio:destroy for infinitescroll");
    console.log("destroying waypoints");
    $(ele).waypoint('destroy');
  });
  function initInfiniteScroll() {
    console.log("in initInfiniteScroll");
    if (nextPage == "") {
      console.log("At end");
      return;
    }
    console.log("numchildren: " + $(ele).children().length);
    var inView = isElementInView($(ele).last(), false);
    if (inView) {
      console.log('in view');
      if (nextPage == "") {
        console.log('at end');
        return;
      }
      runawayCounter++;
      if (runawayCounter > 5) {
        // failsafe to prevent infinite loop of fetching for whatever reason
        console.log("RUNAWAY")
        return
      }
      console.log('loading more');
      loadMore();
      return;
    }
    console.log("setting waypoint");
    thewaypoint = $(ele).last().waypoint(function(direction){
      console.log("in waypoint");
      $(this).waypoint('destroy');
      if(direction === "down") {
        console.log("Loading more")
        loadMore(); 
      }
    }, { offset: '100%'})
  }
  function loadMore(){
    if (nextPage == "") {
      return;
    }
    (function() {
      let urlstr = fixupURL("https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p="+nextPage+"&infinite=1");
      console.log("Fetching:", urlstr);
      num = 0;
      $.ajax({
        url: urlstr,
        cache: false,
        xhrFields: {
            withCredentials: true
        }
      }).done(function( data ) {
        $.each(data.Items, function(i,item) {
          $('#records').append($(item)[0]);
          num++;
        });
        
        console.log("Loaded " + num + " more")
        nextPage = data.NextPage;
        initInfiniteScroll();
      });
    })();
  }

  function isElementInView(element, fullyInView) {
    var pageTop = $(window).scrollTop();
    var pageBottom = pageTop + $(window).height();
    //var elementTop = $(element).offset().top;
    var elementTop = $(element).position().top;
    var elementBottom = elementTop + $(element).height();
  console.log("eletop:" + elementTop);
    if (fullyInView === true) {
        return ((pageTop < elementTop) && (pageBottom > elementBottom));
    } else {
        return ((elementTop <= pageBottom) && (elementBottom >= pageTop));
    }
  }

  if ($("#records").is("table") == true) {
    console.log("is a table");
    ele = "#records tr.test";
  }
  // activate dotdotdot because of dynamically loaded code
  
  if (document.documentElement.clientWidth <= 767) {
    nextPage = "Created%2C%2C%2C20%2C1%2C20%2C0";
    if (nextPage != "") {
      nextPage += "&next=1";
    }
    initInfiniteScroll();
  }

</script>




  
</div>
"""

thread_2 = """<div id="maincontent" class="col-xs-12 col-sm-12 col-md-9 col-lg-10">




	
	


<div id="alertdiv"></div>

<div class="noticetemplate template">
	<div class="alert alert-success alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
		<span id="msg"></span>
	</div>
</div>
<div class="alerttemplate template">
	<div class="alert alert-danger alert-dismissible" role="alert">
		<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
		<span id="msg"></span>
	</div>
</div>
<div class="alertnoclosetemplate template">
	<div class="alert alert-danger" role="alert">
		<span id="msg"></span>
	</div>
</div>



 
<script>
var $alerttemplate = $(".alerttemplate");
var $alertnoclosetemplate = $(".alertnoclosetemplate");
var $noticetemplate = $(".noticetemplate");
function createAlert(msg, isError, autoClose, noClose) {
	if (isError == false) {
		$newPanel = $noticetemplate.clone();
	} else {
        if (noClose) {
		  $newPanel = $alertnoclosetemplate.clone();
        } else {
		  $newPanel = $alerttemplate.clone();
        }
	}
	$newPanel.find("#msg").html(msg);
	if (autoClose == true) {
		$("#alertdiv").append($newPanel.fadeTo(2000, 500).slideUp(500, function(){
		    $newPanel.slideUp(500);
		    $newPanel.remove();
		}));  	
	} else {
		$("#alertdiv").append($newPanel.fadeIn());
	}
    return $newPanel;
}




</script>







<script>
  // doLike toggles a like for a person.
  function doLike(groupname, numlikes, msgid, like, csrf) {
    $.ajax({
      url: groupname+"/like?msgid="+msgid+"&like="+like+"&csrf="+csrf,
      cache: false,
    });
    if (like == true) {
      numlikes++
    } else {
      numlikes--
    }
    displayLikes(groupname, numlikes, msgid, like, csrf);
    displayLikeStats(groupname, numlikes, msgid, like);
  }

  // displayLikes displays the Like/Unlike link button.
  function displayLikes(groupname, numlikes, msgid, hasliked, csrf) {
    console.log("in displayLikes")
    if (hasliked == true) {
      likedata = "<span id='likebutton"+msgid+"'><a href='#' onclick='doLike(\""+groupname+"\","+numlikes+","+msgid+", false, \""+csrf+"\");return false;'><i class=\"fa fa-thumbs-up\"></i> Unlike</a></span>"
    } else {
      likedata = "<span id='likebutton"+msgid+"'><a href='#' onclick='doLike(\""+groupname+"\","+numlikes+","+msgid+", true, \""+csrf+"\");return false;'><i class=\"fa fa-thumbs-up\"></i> Like</a></span>"
    }
    $("#likebutton"+msgid).html(likedata);
  }

  // displayLikeStats displays the line that shows how many people have liked this.
  function displayLikeStats(groupname, numlikes, msgid, hasliked) {
    if (hasliked == false && numlikes == 0) {
      $("#likestats"+msgid).html("<span id='likestats"+msgid+"'></span>");
      return
    }
    likedata = "<span id='likestats" + msgid + "'><i class='fa fa-thumbs-up'></i> "
    if (hasliked == true) {
      likedata += "You"
      if (numlikes > 1) {
        likedata = likedata + " and <a href='#' onclick='showLikes(\"" + groupname + "\"," + msgid + ");return false;'>" + (numlikes-1)
        if (numlikes == 2) {
          likedata = likedata + " other"
        } else {
          likedata = likedata + " others"
        }
      }
    } else {
        likedata += "<a href='#' onclick='showLikes(\"" + groupname + "\"," + msgid + ");return false;'>" + numlikes
        if (numlikes == 1) {
          likedata = likedata + " person"
        } else {
          likedata = likedata + " people"
        }
    }
    likedata = likedata + "</a> liked this</span>"
    $("#likestats"+msgid).html(likedata);
  }

  // showLikes fetches all the likes for a message and pops up the dialog box to show them.
  function showLikes(groupname, msgid) {
    console.log(groupname)
    $.getJSON(fixupURL(groupname+"/getlikes?msgid="+msgid), function( data ) {
        htmldata = '<table class="table the-table table-condensed table-responsive">'
        jQuery.each(data, function() {
          htmldata += '<tr><td valign="center">' + this.Icon + ' ' + this.Profile + '</td></tr>'
        });
        htmldata += '</table>'
        $("#showlikesbody").html(htmldata);
        $('#showlikesmodal').modal({show:true})
      }
    );
  }
</script>

<!-- show likes modal -->
<div class="modal fade" id="showlikesmodal" tabindex="-1" role="dialog" aria-labelledby="showlikesmodalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="showlikesmodalLabel">Likes</h4>
      </div>
      <div class="modal-body">
        <div id="showlikesbody"></div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Close</button>
      </div>
    </div>
  </div>
</div>




<script>
  /**
   * Checks if value is empty. Deep-checks arrays and objects
   * Note: modIsEmpty([]) == true, modIsEmpty({}) == true, modIsEmpty([{0:false},"",0]) == true, modIsEmpty({0:1}) == false
   * @param value
   * @returns {boolean}
   */
  function isEmpty(value) {
    var isEmptyObject = function (a) {
      if (typeof a.length === 'undefined') {
        // it's an Object, not an Array
        var hasNonempty = Object.keys(a).some(function nonEmpty(element) {
          return !isEmpty(a[element]);
        });
        return hasNonempty ? false : isEmptyObject(Object.keys(a));
      }

      return !a.some(function nonEmpty(element) {
        // check if array is really not empty as JS thinks
        return !isEmpty(element); // at least one element should be non-empty
      });
    };
    return (
      value == false ||
      typeof value === 'undefined' ||
      value == null ||
      (typeof value === 'object' && isEmptyObject(value))
    );
  }

var editor = (function () {

  // modDeletedDraft indicates the draft has been deleted, so we shouldn't try to save to it.
  var modDeletedDraft = false;
  var modDestroyedEditor = false;
  var modUnloading = false;

  // uploaderPrompt pops up either the appropriate web dialog, or the camera picker
  function modUploaderPrompt(doctype, id, draftid, groupurl, csrf) {
    console.log("UPLOADERPROMPT: V4");
    console.log("in uploaderPrompt, draftid=", draftid);
    if (typeof Capacitor !== 'undefined') {
      takePicture(doctype, id, draftid, groupurl, csrf);
      return;
    }
    if (doctype == "pictures") {
      $('#addPicturesModal' + id).modal({});
      return;
    } else if (doctype == "attachments") {
      $('#addAttachmentsModal' + id).modal({});
      return
    }
  }


  /**
   * Checks if value is empty. Deep-checks arrays and objects
   * Note: modIsEmpty([]) == true, modIsEmpty({}) == true, modIsEmpty([{0:false},"",0]) == true, modIsEmpty({0:1}) == false
   * @param value
   * @returns {boolean}
   */
  function modIsEmpty(value) {
    var isEmptyObject = function (a) {
      if (typeof a.length === 'undefined') {
        // it's an Object, not an Array
        var hasNonempty = Object.keys(a).some(function nonEmpty(element) {
          return !modIsEmpty(a[element]);
        });
        return hasNonempty ? false : isEmptyObject(Object.keys(a));
      }

      return !a.some(function nonEmpty(element) {
        // check if array is really not empty as JS thinks
        return !modIsEmpty(element); // at least one element should be non-empty
      });
    };
    return (
      value == false ||
      typeof value === 'undefined' ||
      value == null ||
      (typeof value === 'object' && isEmptyObject(value))
    );
  }

  function modDestroyAllEditors(evt) {
    console.log("In modDestroyAllEditors");
    modDestroyedEditor = true;
    while (tinymce.editors.length > 0) {
      console.log("Removing");
      tinymce.remove(tinymce.editors[0]);
    }
    if (retryTimer != null) {
      console.log("clearing retryTimer");
      clearInterval(retryTimer);
    }
    document.body.removeEventListener("gio:destroy", modDestroyAllEditors);
  }

  function modUploadData(draftid, csrf, inline) {
    let obj = {};
    obj['csrf'] = csrf;
    obj['draftid'] = draftid;
    obj['ajaxupload'] = '1';
    obj['upload'] = '1';
    if (inline == true) {
      obj['inline'] = '1';
    }
    return obj;
  }

  // attach the uploader to the correct buttons
  function modInitDeviceUploader(id, draftid, csrf, groupurl) {
  }

  // attach the uploader to the correct buttons
  function modInitWebUploader(id, draftid, csrf, groupurl) {
    if (document.documentElement.clientWidth > 767) {
      $('#attachmentupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, false),
        showClose: false,
        showUpload: false,
        previewFileType: 'any',
        uploadAsync: false,
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
      $('#pictureupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, true),
        showClose: false,
        showUpload: false,
        previewFileType: 'any',
        uploadAsync: false,
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
    } else {
      $('#attachmentupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, false),
        previewFileType: 'any',
        uploadAsync: false,
        showClose: false,
        showUpload: false,
        dropZoneTitle: 'Click folder icon to select files ...',
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
      $('#pictureupload' + id).fileinput({
        uploadUrl: fixupURL(groupurl + '/draftop'),
        uploadExtraData: modUploadData(draftid, csrf, true),
        previewFileType: 'any',
        uploadAsync: false,
        showClose: false,
        showUpload: false,
        dropZoneTitle: 'Click folder icon to select files ...',
        fileActionSettings: {
          indicatorNew: ''
        },
        slugCallback: function (text) {
          return modIsEmpty(text)
            ? ''
            : String(text).replace(
              /[\[\]\/\{}:;#%=\(\)\*\+\?\\\^\$\|<>&"']/g,
              '_'
            );
        },
        maxFileSize: 1073741824
      });
    }
    $('#attachmentupload' + id).on('filebatchuploadcomplete', function (
      event,
      files,
      extra
    ) {
      console.log('File batch upload complete');
      modUpdateAttachments(id, draftid, csrf, groupurl);
      $('#addAttachmentsModal' + id).modal('hide');
      $('#attachmentupload' + id).fileinput('clear');
    });
    $('#pictureupload' + id).on('filebatchuploadsuccess', function (
      event,
      data,
      previewId,
      index
    ) {
      let files = data.response;
      console.log('Picture file batch upload complete');
      for (var i = files.length - 1; i >= 0; i--) {
        fileurl = files[i];
        console.log('FILE: ' + files[i]);
        console.log('URL: ' + fileurl);
        imghtml = '<img src="' + fileurl + '"/>';
        console.log('imghtml: ' + imghtml);
        tinymce.activeEditor.insertContent(imghtml);
      }
      $('#addPicturesModal' + id).modal('hide');
      $('#pictureupload' + id).fileinput('clear');
    });
  }

  function modUpdateAttachments(id, draftid, csrf, groupurl) {
    // call the real function after 3 seconds to allow S3 to do whatever it needs to do to update
    // results
    setTimeout(function () { modDoUpdateAttachments(id, draftid, csrf, groupurl); }, 3000);
  }
  // modDoUpdateAttachments fetches a list of attachments and displays them on the page.
  function modDoUpdateAttachments(id, draftid, csrf, groupurl) {
    console.log('in modUpdateAttachments');
    upload = { draftid: draftid, csrf: csrf, list: '1' };
    $.ajax({
      url: fixupURL(groupurl + '/draftop'),
      cache: false,
      data: upload,
      method: 'POST',
      xhrFields: {
        withCredentials: true
      },
      dataType: 'json',
      error: function (xhr, ajaxOptions, thrownError) {
        if (modDeletedDraft == false && modDestroyedEditor == false) {
          createAlert("There was an error saving the draft. Please reload the page.", true, false)
        }
      }
    }).done(function (response) {
      // Do something with the request
      console.log('update attachments');
      // reload the page now
      if (response == null) {
        $('#attachments' + id).replaceWith(
          "<div id='attachments" + id + "'></div>"
        );
      } else {
        wrap = '<div id="attachments' + id + '">Attachments:<ul>';
        count = 0;
        for (i = 0; i < response.length; i++) {
          if (response[i].Inline == false) {
            wrap +=
              '<li>' +
              response[i].Name +
              ' (' +
              response[i].Size +
              ') <a href=\'javascript:deleteAttachment("' +
              id +
              '","' +
              draftid +
              '","' +
              csrf +
              '","' +
              groupurl +
              '","' +
              response[i].Num +
              "\")'><i class='fa fa-times'></i></a></li>";
            count++;
          }
        }
        wrap += '</ul><br /></div>';
        if (count > 0) {
          $('#attachments' + id).replaceWith(wrap);
        } else {
          $('#attachments' + id).replaceWith(
            "<div id='attachments" + id + "'></div>"
          );
        }
      }
    });
  }

  var modTimeoutId;
  function modOnFormChange(id, draftid, groupurl, csrf) {
    clearTimeout(modTimeoutId);
    if (modSaving == true) {
      modTimeoutId = setTimeout(function () {
        // Runs 1 second (1000 ms) after the last change
        modOnFormChange(id, draftid, groupurl, csrf);
      }, 1000);
      return;
    }
    modTimeoutId = setTimeout(function () {
      // Runs 1 second (1000 ms) after the last change
      modSaveDraft(id, draftid, groupurl, csrf, false);
    }, 1000);
  }

  var modSaving = false;

  // modSaveDraft saves the current form state in the draft.
  function modSaveDraft(id, draftid, groupurl, csrf, onLeave) {
    if (draftid == 0) {
      console.log("DraftID 0, not modSaving");
      return;
    }
    console.log("DELETEDDRAFT IS:", modDeletedDraft);
    console.log("DESTROYEDEDITOR IS:", modDestroyedEditor);
    if (modDeletedDraft == true) {
      console.log('NOT SAVING BECAUSE OF DELETED');
      return;
    }
    if (modDestroyedEditor == true) {
      console.log('NOT SAVING BECAUSE OF DESTROYED');
      return;
    }
    modSaving = true;
    console.log('modSaving');
    var fromval = $('#from' + id).val();
    var subject = $('#subject' + id).val();
    var body = $('#editor' + id).val();
    var bodytype = $('#bodytype' + id).val();
    var private = $('#isprivate' + id).val();
    var special = '0';
    if ($('#special').prop('checked') == true) {
      special = '1';
    }
    var bccme = '0';
    if ($('#bccme').prop('checked') == true) {
      bccme = '1';
    }
    var bccall = '0';
    if ($('#bccall').prop('checked') == true) {
      bccall = '1';
    }
    var saveval = '1';
    if (onLeave == true) {
      saveval = '2';
    }
    var hashtags = $('#hashtags').val();
    upload = {
      draftid: draftid,
      csrf: csrf,
      from: fromval,
      subject: subject,
      body: body,
      bodytype: bodytype,
      special: special,
      private: private,
      bccme: bccme,
      bccall: bccall,
      hashtags: JSON.stringify(hashtags),
      mid: id,
      save: saveval
    };
    let opts = {
      url: fixupURL(groupurl + '/draftop'),
      cache: false,
      data: upload,
      method: 'POST',
      xhrFields: {
        withCredentials: true
      },
      dataType: 'json'
    };
    if (modUnloading == false) {
      // if we are unloading we don't want to retry, because sometimes
      // that can result in a spurious error, esp on Firefox
      opts.retryCount = 5;
      opts.retryVerify = modRetryVerify;
    }
    $.ajax(opts).done(function (response) {
      // Do something with the request
      console.log('saved');
      modSaving = false;
    });
  }

  // called to see if we need to continue retrying
  function modRetryVerify() {
    if (modDeletedDraft == true || modDestroyedEditor == true) {
      return false;
    }
    return true;
  }

  // stop modSaving drafts when we do a submit
  var postVar = null;

  // Code to find and return a selected piece of HTML.
  function modGetSelection(id) {
    var flag = 0;
    var sel = document.getSelection();
    var selText = '';
    id = 'msgbody' + id;
    var forkfork = document.getElementById(id);
    if (sel.rangeCount > 0) {
      var range = sel.getRangeAt(0);
      var test = range.cloneContents();
      var clonedSelection = '';
      if (typeof test.getElementByID != 'undefined') {
        clonedSelection = range.cloneContents().getElementById(id);
      }
      if (clonedSelection) {
        selText = clonedSelection.innerHTML;
      } else {
        clonedSelection = range.cloneContents();
        var startNode = sel.getRangeAt(0).startContainer.parentNode;
        //console.log(modIsChild(startNode, forkfork));
        if (modIsChild(startNode, forkfork)) {
          var div = document.createElement('div');
          div.appendChild(clonedSelection);
          selText = div.innerHTML;
        }
      }
    }

    return selText.toString();
  }
  function modIsChild(child, parent) {
    if (child === parent) return true;
    var current = child;
    while (current) {
      if (current === parent) return true;
      current = current.parentNode;
    }
    return false;
  }


  return {

    InitEditor: function (
      id,
      editorType,
      draftid,
      groupurl,
      csrf,
      handleAttachments,
      noFontChanges,
      isReply,
      isWiki,
      sig,
      onInitFunc
    ) {
      if (typeof onInitFunc === 'undefined') { onInitFunc = null; }

      //document.getElementById("editor" + id).addEventListener("gio:destroy", modDestroyAllEditors);
      document.body.addEventListener("gio:destroy", modDestroyAllEditors);
      modDeletedDraft = false;
      modDestroyedEditor = false;
      modUnloading = false;

      $('#preview' + id).hide();
      $('#addattachments' + id).hide();
      $('#return' + id).hide();
      $('#markdownlink' + id).hide();
      if (editorType == 'html') {
        if (sig != '') {
          $('#editor' + id).val(sig);
          //tinyMCE.get('editor'+id).setContent(sig);
        }
        editor.initHTMLEditor(
          id,
          draftid,
          groupurl,
          csrf,
          handleAttachments,
          noFontChanges,
          isReply,
          isWiki,
          sig,
          onInitFunc
        );
      } else {
        if (sig != '') {
          $('#editor' + id).val(sig);
        }
        editor.initPlainEditor(id, editorType);
      }
    },

    initHTMLEditor: function (
      id,
      draftid,
      groupurl,
      csrf,
      handleAttachments,
      noFontChanges,
      isReply,
      isWiki,
      sig,
      onInitFunc
    ) {

      if (typeof onInitFunc === 'undefined') { onInitFunc = null; }
      // extras: print, emoticons, image, insert, media, print
      /* All plugins:
              'advlist autolink lists link image print preview hr anchor pagebreak',
          'searchreplace wordcount visualblocks visualchars code fullscreen',
          'insertdatetime media nonbreaking save table contextmenu directionality',
          'emoticons template paste textcolor colorpicker textpattern imagetools codesample toc'
      */
      modDeletedDraft = false;
      modDestroyedEditor = false;
      modUnloading = false;
      let attachments = '';
      if (handleAttachments == 0 || handleAttachments == 3) {
        attachments = ' addPictures addAttachments';
      }
      let fontchanges = '';
      if (noFontChanges == false) {
        fontchanges = ' fontselect fontsizeselect forecolor backcolor';
      }
      let fontawesome = ' charmap';
      let forceRootBlock = false;
      if (isWiki == true) {
        attachments += ' addWikiImage addWikiLink addWikiTOC';
        fontawesome = ' fontawesome';
        // BORK
        fontawesome = '';
        forceRootBlock = 'p';
      }
      let toolbar1 =
        'styleselect bold italic bullist numlist link blockquote alignleft aligncenter alignright' +
        attachments +
        ' advancedToolbar';
      let toolbar2 =
        'strikethrough underline hr alignjustify' +
        fontchanges +
        ' removeformat' +
        fontawesome +
        ' outdent indent undo redo preview code';

      let small_toolbar1 =
        'bold italic link blockquote' + attachments + ' advancedToolbar';
      let small_toolbar2 =
        'strikethrough underline hr alignjustify removeformat outdent indent';

      let tm_fonts =
        'Arial=arial,helvetica,sans-serif;' +
        'Arial Black=arial black,avant garde;' +
        'Comic Sans MS=comic sans ms;' +
        'Courier Neue=courier_newregular,courier;' +
        'Helvetica Neue=helvetica neue;' +
        'Helvetica=helvetica;' +
        'Impact=impactregular,chicago;' +
        'Lucida Grande=lucida grande;' +
        'Tahoma=tahoma,arial,helvetica,sans-serif;' +
        'Times New Roman=times new roman,times;' +
        'Verdana=verdana,geneva';
      let plugins = [
        'SplitBlockquote',
        'advlist autolink lists link image preview hr anchor',
        'code fullscreen',
        'nonbreaking table charmap',
        'textcolor colorpicker imagetools noneditable'
      ];
      let css =
        fixupURL('/bootstrap/3.3.6/css/bootstrap.min.css') + ',' + fixupURL('/bootstrap/3.3.6/css/bootstrap-theme.min.css') + ',' + fixupURL('/css/groupsio.css') + ',' + fixupURL('/css/tinymce.css') + ',' + fixupURL('/fontawesome/5.9.0/css/all.min.css');

      let fontsizes = '8pt 10pt 11pt 12pt 14pt 18pt 24pt 36pt';

      let codesample_languages = [
        { text: 'C', value: 'c' },
        { text: 'C#', value: 'csharp' },
        { text: 'C++', value: 'cpp' },
        { text: 'CSS', value: 'css' },
        { text: 'Go', value: 'go' },
        { text: 'HTML/XML', value: 'markup' },
        { text: 'Java', value: 'java' },
        { text: 'JavaScript', value: 'javascript' },
        { text: 'PHP', value: 'php' },
        { text: 'Python', value: 'python' },
        { text: 'Ruby', value: 'ruby' }
      ];

      let style_formats = [
        { title: 'Paragraph', block: 'p' },
        { title: 'Header 1', block: 'h1' },
        { title: 'Header 2', block: 'h2' },
        { title: 'Header 3', block: 'h3' },
        { title: 'Header 4', block: 'h4' },
        { title: 'Header 5', block: 'h5' },
        { title: 'Header 6', block: 'h6' }
      ];

      if (isReply == true) {
        toolbar1 = 'quoteMessage ' + toolbar1;
        small_toolbar1 = 'quoteMessage ' + small_toolbar1;
      }
      if (document.documentElement.clientWidth > 1000) {
        tinymce.init({
          noneditable_noneditable_class: 'fa',
          extended_valid_elements: 'span[*]',
          branding: false,
          link_context_toolbar: true,
          default_link_target: '_blank',
          link_assume_external_targets: true,
          elementpath: false,
          forced_root_block: forceRootBlock,
          content_css: css,
          relative_urls: false,
          remove_script_host: false,
          menubar: false,
          statusbar: true,
          plugins: plugins,
          toolbar1: toolbar1,
          toolbar2: toolbar2,
          font_formats: tm_fonts,
          browser_spellcheck: true,
          contextmenu: false,
          selector: '#editor' + id,
          resize: true,
          fontsize_formats: fontsizes,
          style_formats: style_formats,
          setup: function (teditor) {
              teditor.on('Init', function (e) {
              if (sig != "") {
                teditor.setContent(sig);
              } else {
                setContent(teditor);
              }
              });
            if (onInitFunc != null) {
              teditor.on('Init', function (e) {
                onInitFunc(e);
              });
            }
            teditor.on('BeforeRenderUI', function (e) {
              teditor.theme.panel
                .find('toolbar')
                .slice(1)
                .hide();
            });
            teditor.addButton('advancedToolbar', {
              tooltip: 'Show advanced toolbar',
              icon: 'fa fa-bars',
              onclick: function () {
                if (!this.active()) {
                  this.active(true);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .show();
                } else {
                  this.active(false);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .hide();
                }
              }
            });
            teditor.addButton('addPictures', {
              tooltip: 'Add pictures',
              icon: 'fa fa-image',
              onclick: function () {
                modUploaderPrompt("pictures", id, draftid, groupurl, csrf);
              }
            });
            teditor.addButton('addAttachments', {
              tooltip: 'Add attachments',
              icon: 'fa fa-paperclip',
              onclick: function () {
                modUploaderPrompt("attachments", id, draftid, groupurl, csrf);
              }
            });
            if (groupurl != '') {
              teditor.addButton('quoteMessage', {
                tooltip: 'Quote post',
                icon: 'fa fa-comment',
                onclick: function () {
                  editor.ShowMessageHistory(id, groupurl, 'html', '', sig, false);
                }
              });
            }
            if (draftid != '' && draftid != '0' && draftid != 0) {
              teditor.on('NodeChange', function () {
                //tinymce.triggerSave();
                if (tinymce.activeEditor != null) {
                  let markupStr = tinymce.activeEditor.getContent();
                  $('#editor' + id).val(markupStr);
                  modOnFormChange(id, draftid, groupurl, csrf);
                }
              });
              teditor.on('keyup', function () {
                //tinymce.triggerSave();
                let markupStr = tinymce.activeEditor.getContent();
                $('#editor' + id).val(markupStr);
                modOnFormChange(id, draftid, groupurl, csrf);
              });
            }
            if (isWiki == true) {
              // special wiki buttons
              teditor.addButton('addWikiImage', {
                tooltip: 'Insert image',
                icon: 'fa fa-image',
                onclick: function () {
                  $('#ImageModal').modal({});
                }
              });
              teditor.addButton('addWikiLink', {
                tooltip: 'Insert link to wiki page',
                icon: 'fa fa-book',
                onclick: function () {
                  $('#LinkModal').modal({});
                }
              });
              teditor.addButton('addWikiTOC', {
                tooltip: 'Insert table of contents',
                icon: 'fa fa-list-alt',
                onclick: function () {
                  $('#TOCModal').modal({});
                }
              });
            }
          }
        });
      } else {
        tinymce.init({
          branding: false,
          link_context_toolbar: true,
          default_link_target: '_blank',
          link_assume_external_targets: true,
          elementpath: false,
          forced_root_block: forceRootBlock,
          content_css: css,
          relative_urls: false,
          remove_script_host: false,
          menubar: false,
          statusbar: true,
          plugins: plugins,
          toolbar1: small_toolbar1,
          toolbar2: small_toolbar2,
          font_formats: tm_fonts,
          browser_spellcheck: true,
          contextmenu: false,
          selector: '#editor' + id,
          resize: true,
          fontsize_formats: fontsizes,
          style_formats: style_formats,
          setup: function (teditor) {
              teditor.on('Init', function (e) {
              if (sig != "") {
                teditor.setContent(sig);
              } else {
                setContent(teditor);
              }
              });
            if (onInitFunc != null) {
              teditor.on('Init', function (e) {
                onInitFunc(e);
              });
            }
            teditor.on('BeforeRenderUI', function (e) {
              teditor.theme.panel
                .find('toolbar')
                .slice(1)
                .hide();
            });
            teditor.addButton('advancedToolbar', {
              tooltip: 'Show advanced toolbar',
              icon: 'fa fa-bars',
              onclick: function () {
                if (!this.active()) {
                  this.active(true);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .show();
                } else {
                  this.active(false);
                  teditor.theme.panel
                    .find('toolbar')
                    .slice(1)
                    .hide();
                }
              }
            });
            teditor.addButton('addPictures', {
              tooltip: 'Add pictures',
              icon: 'fa fa-image',
              onclick: function () {
                modUploaderPrompt("pictures", id, draftid, groupurl, csrf);
              }
            });
            teditor.addButton('addAttachments', {
              tooltip: 'Add attachments',
              icon: 'fa fa-paperclip',
              onclick: function () {
                modUploaderPrompt("attachments", id, draftid, groupurl, csrf);
              }
            });
            if (groupurl != '') {
              teditor.addButton('quoteMessage', {
                tooltip: 'Quote post',
                icon: 'fa fa-comment',
                onclick: function () {
                  editor.ShowMessageHistory(id, groupurl, 'html', '', sig, false);
                }
              });
            }
            if (draftid != '' && draftid != '0' && draftid != 0) {
              teditor.on('NodeChange', function () {
                if (tinymce.activeEditor != null) {
                  //tinymce.triggerSave();
                  let markupStr = tinymce.activeEditor.getContent();
                  $('#editor' + id).val(markupStr);
                  modOnFormChange(id, draftid, groupurl, csrf);
                }
              });
              teditor.on('keyup', function () {
                //tinymce.triggerSave();
                let markupStr = tinymce.activeEditor.getContent();
                $('#editor' + id).val(markupStr);
                modOnFormChange(id, draftid, groupurl, csrf);
              });
            }
            // special wiki buttons
            teditor.addButton('addWikiImage', {
              tooltip: 'Add Image',
              icon: 'fa fa-image',
              onclick: function () {
                $('#ImageModal').modal({});
              }
            });
            teditor.addButton('addWikiLink', {
              tooltip: 'Add Link',
              icon: 'fa fa-book',
              onclick: function () {
                $('#LinkModal').modal({});
              }
            });
            teditor.addButton('addWikiTOC', {
              tooltip: 'Table of Contents',
              icon: 'fa fa-list-alt',
              onclick: function () {
                $('#TOCModal').modal({});
              }
            });
          }
        });

        // disable tooltips because they require double taps on mobile
        $('.note-editor *').tooltip('disable');
      }
    },

    initPlainEditor: function (id, editorType, handleAttachments) {
      $('#addattachments').show();
      if (editorType == 'plain') {
        $('#bodytype' + id).val('plain');
        $('#preview' + id).hide();
        $('#return' + id).hide();
        $('#preview' + id).hide();
        $('#markdownlink' + id).hide();
      } else {
        $('#bodytype' + id).val('markdown');
        $('#markdownbuttons' + id).show();
        $('#preview' + id).show();
        $('#return' + id).hide();
        $('#previewWindow' + id).hide();
        $('#markdownlink' + id).show();
      }
    },

    InitPostDraft: function (id, draftid, csrf, groupurl) {
      // save the draft when leaving the page.
      $(window).on('beforeunload', function () {
        modUnloading = true;
        modSaveDraft(id, draftid, groupurl, csrf, true);
      });

      // save the draft 1 second after a change
      $('form input, form textarea').on('input propertychange change', function () {
        modOnFormChange(id, draftid, groupurl, csrf);
      });
      modUpdateAttachments(id, draftid, csrf, groupurl);

      if (typeof Capacitor !== 'undefined') {
        modInitDeviceUploader(id, draftid, csrf, groupurl);
      } else {
        modInitWebUploader(id, draftid, csrf, groupurl);
      }
    },

    // InitReplyDraft creates a new draft, assumes a hidden form input called #draftidmid, and then calls initWindow().
    InitReplyDraft: function (
      id,
      bodytype,
      draftid,
      groupurl,
      csrf,
      handleAttachments,
      noFontChanges,
      sig
    ) {
      console.log('in InitReplyDraft draftid=' + draftid);
      modDeletedDraft = false;
      modDestroyedEditor = false;
      modUnloading = false;

      if (draftid == 0) {
        // create a new draft
        console.log('generating new draft' + groupurl);
        console.log('id=' + id);
        upload = { mid: id, csrf: csrf, body: sig };
        $.ajax({
          url: fixupURL(groupurl + '/reply'),
          cache: false,
          method: 'POST',
          data: upload,
          xhrFields: {
            withCredentials: true
          },
          dataType: 'json',
          error: function (xhr, ajaxOptions, thrownError) {
            if (modDeletedDraft == false && modDestroyedEditor == false) {
              createAlert("There was an error saving the draft. Please reload the page.", true, false)
            }
          }
        }).done(function (response) {
          console.log('reply draft created');
          console.log('draftid:' + response.DraftID);
          draftid = response.DraftID;
          toquote = modGetSelection(id);
          if (toquote != '') {
            console.log('id=' + id);
            editor.ShowMessageHistory(id, groupurl, bodytype, toquote, sig, true);
          }
          $('#draftid' + id).val(response.DraftID);
          editor.InitEditor(
            id,
            bodytype,
            draftid,
            groupurl,
            csrf,
            handleAttachments,
            noFontChanges,
            true,
            false,
            sig
          );
          editor.InitPostDraft(id, draftid, csrf, groupurl);
          console.log('id=' + id);
          $('#bodytype' + id).val(bodytype);
          $('#cancel-' + id).attr(
            'onclick',
            'editor.discardReplyDraft("' +
            id +
            '", "' +
            draftid +
            '","' +
            bodytype +
            '","' +
            csrf +
            '","' +
            groupurl +
            '");'
          );
          return;
        });
        return;
      }
      editor.InitEditor(
        id,
        bodytype,
        draftid,
        groupurl,
        csrf,
        handleAttachments,
        noFontChanges,
        true,
        false,
        sig
      );
      editor.InitPostDraft(id, draftid, csrf, groupurl);
      $('#bodytype' + id).val(bodytype);
      $('#cancel-' + id).attr(
        'onclick',
        'editor.discardReplyDraft("' +
        id +
        '", "' +
        draftid +
        '","' +
        bodytype +
        '","' +
        csrf +
        '","' +
        groupurl +
        '");'
      );
      console.log('DONE');
    },

    // discardReplyDraft deletes the draft and any attachments and returns the user to the previous page.
    discardReplyDraft: function (id, draftid, bodytype, csrf, groupurl) {
      console.log('editor delete reply draft');
      upload = { draftid: draftid, csrf: csrf, jsondelete: '1' };
      $.ajax({
        url: fixupURL(groupurl + '/draftop'),
        cache: false,
        data: upload,
        method: 'POST',
        xhrFields: {
          withCredentials: true
        },
        dataType: 'json'
      }).done(function (response) {
        // Do something with the request
        console.log("success delete reply draft");
        $('#draftid' + id).val('');
        if (bodytype == 'html') {
          tinymce.get('editor' + id).remove();
        }
        $('#subject' + id).val($('#origsubject' + id).val());
        $('#editor' + id).val('');
        modDeletedDraft = true;
        modDestroyedEditor = true;
      });
    },

    PreviewMarkdown: function (id, groupurl) {
      let markdown = $('#editor' + id).val();
      upload = { md: markdown };
      $.ajax({
        url: fixupURL(groupurl + '/previewmd'),
        cache: false,
        data: upload,
        method: 'POST',
        xhrFields: {
          withCredentials: true
        },
        dataType: 'json'
      }).done(function (response) {
        // Do something with the request
        console.log(response.markdown);
        wrap =
          '<div id="previewWindow' +
          id +
          '"><div class="well well-sm">' +
          response.markdown +
          '</div></div>';
        $('#editwindow' + id).hide();
        $('#previewWindow' + id).replaceWith(wrap);
        $('#previewWindow' + id).show();
      });

      $('#preview' + id).hide();
      $('#return' + id).show();
    },

    ReturnMarkdown: function (id) {
      $('#preview' + id).show();
      $('#return' + id).hide();
      $('#previewWindow' + id).hide();
      $('#editwindow' + id).show();
    },

    // groupReplyto is groupsio.ReplyTo
    // toggle=0 is group
    // toggle=1 is sender
    // toggle=2 is mods
    TogglePrivate: function (id, groupReplyto, toggle) {
      console.log("in TogglePrivate");
      if (groupReplyto == 2) {
        // Reply To Moderators
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').removeClass('btn-info').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 2);return false;");
          $('#grouptoggle' + id).removeClass('btn-success').addClass('btn-default');
          $('#grouptoggle' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else if (toggle == 2) {
          $('#replytype' + id).val('mods');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Mods</a>');
          $('#replybutton' + id).removeClass('btn-success').removeClass('btn-primary').addClass('btn-info');
          $('#grouptoggle' + id).removeClass('btn-success').addClass('btn-default');
          $('#grouptoggle' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group');
          $('#replybutton' + id).removeClass('btn-primary').removeClass('btn-info').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 2);return false;");
          $('#grouptoggle' + id).removeClass('btn-default').addClass('btn-success');
          $('#grouptoggle' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 2);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else if (groupReplyto == 1) {
        // Reply To Sender
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-success').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-default').addClass('btn-success');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else if (groupReplyto == 3) {
        // Reply To Group And Sender
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group & Sender');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else if (groupReplyto == 5) {
        // Reply To Followers Only
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Topic Followers Only');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      } else {
        if (toggle == 1) {
          $('#replytype' + id).val('sender');
          $('#isprivate' + id).val('1');
          $('#replybutton' + id).html('<i class="fa fa-user"></i> Reply to Sender');
          $('#replybutton' + id).removeClass('btn-success').addClass('btn-primary');
          $('#private' + id).removeClass('btn-default').addClass('btn-primary');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 0);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val('Private: ' + subj);
          $('#bccme' + id).show();
        } else {
          $('#replytype' + id).val('group');
          $('#isprivate' + id).val('');
          $('#replybutton' + id).html('<i class="fa fa-reply"></i> Reply to Group');
          $('#replybutton' + id).removeClass('btn-primary').addClass('btn-success');
          $('#private' + id).removeClass('btn-primary').addClass('btn-default');
          $('#private' + id).attr('onclick', "editor.TogglePrivate('" + id + "','" + groupReplyto + "', 1);return false;");
          subj = $('#subject' + id).val();
          $('#subject' + id).val(subj.replace('Private: ', ''));
          $('#bccme' + id).hide();
        }
      }
    },

    ClearTimeout: function() {
      clearTimeout(modTimeoutId);
    },

    ShowMessageHistory: function(
      id,
      groupurl,
      bodytype,
      selectedText,
      sig,
      firstTime
    ) {
      console.log('URL ' + groupurl);
      console.log('ID ' + id);
      if (bodytype == 'html' && firstTime == false) {
        existingmsg = tinyMCE.get('editor' + id).getContent();
      } else {
        existingmsg = $('#editor' + id).val();
      }
      if (selectedText == '') {
        upload = { preview: bodytype, id: id };
      } else {
        upload = { preview: bodytype, id: id, text: selectedText };
        if (firstTime == true) {
          existingmsg = sig;
        }
      }
      $.ajax({
        url: fixupURL(groupurl + '/previewmd'),
        cache: false,
        data: upload,
        method: 'POST',
        xhrFields: {
          withCredentials: true
        },
        dataType: 'json'
      }).done(function (response) {
        $('#editor' + id).val(response.reply + existingmsg);
        if (bodytype == 'html') {
          console.log('SETTING ' + response.reply + existingmsg);
          tinyMCE.get('editor' + id).setContent(response.reply + existingmsg);
          console.log('DONE');
        }
      });
      $('#editor' + id).focus();
    }




    /*
    $('form').submit(function(e) {
      clearTimeout(modTimeoutId);
      if (postVar != null) {
        postVar.abort();
      }
      console.log("SETTING DELETED TO TRUE");
      console.log("EVENT:", e);
      modDeletedDraft = true;
      if ($(this).hasClass('form-submitted')) {
        e.preventDefault();
        return;
      }
      $(this).addClass('form-submitted');
    });
    */
  };
}());
</script>


<form class="form-inline pull-right hidden-xs" method="get" action="https://ctolunches.groups.io/g/worldwide/search">
  <input type="hidden" name="p" value="Created,,,20,1,20,0">
  <div class="input-group">
    <input type="text" class="form-control" placeholder="Search" title="Search" name="q" size="20" value="">
    <div class="input-group-btn">
      <button class="btn btn-primary" type="submit">
        <span class="fa fa-search"></span>
      </button>
    </div>
  </div>
</form>


<span class="hidden-sm hidden-md hidden-lg pull-right" style="padding:8px 15px;"><a data-toggle="modal" data-target="#searchModal"><i class="fa fa-search"></i></a></span>
<ol class="breadcrumb">
  <li class="hidden-xs"><a href="https://ctolunches.groups.io/g/worldwide"><i class="fa fa-home"></i> worldwide@ctolunches.groups.io</a></li>
  <li><a href="https://ctolunches.groups.io/g/worldwide/topics?p=,,,0,0,0,0"><i class="fa fa-inbox"></i> Topics</a></li>
	
	<li class="active"><i class="fa fa-comments"></i> re-builds</li>
</ol>


<div class="modal fade" id="searchModal" tabindex="-1" role="dialog" aria-labelledby="searchModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
        <h4 class="modal-title" id="searchModalLabel">Search</h4>
      </div>
      <form class="form-horizontal" method="get" action="https://ctolunches.groups.io/g/worldwide/search">
        <div class="modal-body">
            <div class="form-group">
              <div class="col-sm-12">
                <input type="text" class="form-control" placeholder="Search" title="Search" name="q" value="">
              </div>
            </div>
        </div>
        <div class="modal-footer">
          <button class="btn btn-primary btn-sm"><i class="fa fa-search"></i> Search</button>
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        </div>
      </form>
    </div>
  </div>
</div>



  <div class="form-group">
  


  
    <a class="btn btn-info btn-sm bottom10" href="https://ctolunches.groups.io/g/worldwide/ft/90710568?csrf=5276883099450123193&amp;mute=1&amp;p=Created%2C%2C%2C20%2C1%2C20%2C0"><i class="far fa-volume-mute"></i> Mute This Topic</a>
  

  </div>


<div class="pull-right">
  <span class="hidden-xs" style="float:left; margin-top:8px;">
    
      <a href="https://ctolunches.groups.io/g/worldwide/topic/90710568?p=Created%2C%2C%2C20%2C2%2C0%2C0">Date <i class="fa fa-sort-up"></i></a>
    
    &nbsp;&nbsp;
  </span>
  <span class="hidden-sm hidden-md hidden-lg">
    
      <a href="https://ctolunches.groups.io/g/worldwide/topic/90710568?p=Created%2C%2C%2C20%2C2%2C0%2C0">Date <i class="fa fa-sort-up"></i></a>
    
  </span>

  
	
		<span class="hidden-xs">
			<span style="float:left; margin-top:8px;">
				
					21 - 34 of 34
				
			</span>&nbsp;
			<ul class="pagination" style="margin: 0px !important;">
				
					<li><a href="https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p=Created%2C%2C%2C20%2C1%2C0%2C0&amp;prev=1"><i class="fa fa-chevron-left"><span class="sr-only">previous page</span></i></a></li>
				
				
					<li class="disabled"><a href="#"><i class="fa fa-chevron-right"><span class="sr-only">next page</span></i></a></li>
				
			</ul>
		</span>
	


</div>

  <h4>
    
    
    
    re-builds
    
    
  </h4>


<table id="records" class="table table-condensed table-striped table-fixed">
  <tbody><tr></tr>

    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5184"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <img src="https://ctolunches.groups.io/g/worldwide/profilephoto/9890941" width="40" height="40" class="img-rounded">
    
    
  
	
    Ghazenfer Mansoor
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 1:39pm">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5184"><span class="hidden-xs">#5184&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204209180">
        <div class="forcebreak" dir="auto"><div dir="ltr">Dan,&nbsp;<div>In addition to the problems you mentioned, do you also have a problem with the current state of the application, or is it quite stable? I prefer "re-build while flying" because you can gradually build instead of building a brand new system with tons of new features that may also take a long time to build, and then migrate.&nbsp; In my experience, "re-build while flying" keeps users engaged and has a better outcome from business perspectives.&nbsp;I would build a new front-end with a combination of new and existing API, maybe proxy/delegate in some cases, <span class="ng">especially</span>&nbsp;for new modules.</div><div><br></div><div><div dir="ltr"><div><div><div style="font-family:arial,sans-serif;  font-size:13px;"><span style="font-family:Arial,sans-serif;">Ghazenfer Mansoor</span></div><div dir="ltr" style="font-family:arial,sans-serif;  font-size:13px;"><div><div><div><div style="max-width:590px;  font-family:Arial,sans-serif;"><div dir="ltr"><div><div><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr">(W):&nbsp;703.444.0505 x 101&nbsp;<br><a href="mailto:gmansoor@technologyrivers.com" target="_blank" rel="nofollow noopener">gmansoor@technologyrivers.com</a><br><a href="https://www.linkedin.com/in/gmansoor/" target="_blank" rel="nofollow noopener">LinkedIn</a>&nbsp;|&nbsp;&nbsp;<a href="https://www.facebook.com/gmansoor" target="_blank" rel="nofollow noopener">Facebook</a>&nbsp;|&nbsp;<a href="https://twitter.com/gmansoor" target="_blank" rel="nofollow noopener">Twitter</a><wbr>&nbsp;|&nbsp;&nbsp;<a href="https://www.instagram.com/techrivers/" target="_blank" rel="nofollow noopener">Instagram</a><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener"></a>&nbsp;|&nbsp;<a href="https://medium.com/@gmansoor" target="_blank" rel="nofollow noopener">Medium</a>&nbsp;</div><div dir="ltr"><br>Technology Rivers LLC:</div><div dir="ltr"><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener">Web</a>&nbsp;|&nbsp;<a href="https://www.linkedin.com/company/technology-rivers-llc/" target="_blank" rel="nofollow noopener">LinkedIn</a>&nbsp;|&nbsp;<a href="https://www.instagram.com/techrivers/" target="_blank" rel="nofollow noopener">Instagram</a><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener"></a>&nbsp;|&nbsp;<a href="https://twitter.com/techrivers" target="_blank" rel="nofollow noopener">T<wbr>witter</a>&nbsp;|&nbsp;&nbsp;<a href="https://www.facebook.com/techrivers" target="_blank" rel="nofollow noopener">Facebook</a>&nbsp;<a href="https://medium.com/@gmansoor" target="_blank" rel="nofollow noopener"></a>|&nbsp;<a href="https://www.youtube.com/channel/UCqU2dUudlTP1djS9zxAsYIw/" target="_blank" rel="nofollow noopener">YouTube</a>&nbsp;|<wbr>&nbsp;<a href="https://technologyrivers.com/reviews" target="_blank" rel="nofollow noopener">Reviews</a>&nbsp;|&nbsp;<a href="https://technologyrivers.com/our-work" target="_blank" rel="nofollow noopener">Our Work</a></div><div dir="ltr"><br></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div><div><div><div style="max-width:590px;  font-family:Arial,sans-serif;"></div></div><div><div><font color="#3333FF"><i></i></font></div></div></div></div></div></div></div><img align="left" width="0" height="0" style="width:0px;" src="https://technologyrivers.mxspruce.com/api/track/v2/DBJruJdPmmmthgJLf/gIt92YuMnclZXayl3Zvx2buh2YlRHQy92bz5WYtdmI/Iybp5ycwV3bydmLzVGaj5Wds9GdjBUZkl2dkxmcvdnI/ISZkl2dkxmcvdnI?sc=false" alt="" class="myimg-responsive"> <div style="max-width:590px;"> <p><br></p> <div class="gmail_extra"> <p><br></p></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204209180" role="button" data-toggle="collapse" href="#quoted-204209180" aria-expanded="false" aria-controls="quoted-204209180"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204209180" class="collapse forcebreak">
            <div dir="auto"><div class="gmail_quote"> On Tue, Apr 26, 2022 at 11:27 AM Dan Richards <span dir="ltr"> &lt;<a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>&gt;</span> wrote:<br> <blockquote class="gmail_quote"> <u></u> <div>I have a client I've been consulting with for a couple years.&nbsp; They are not a software company, but they have ended up in the software business by building an internal application and then they eventually started selling it to clients and now they have:</div> <ul> <li>A 10+ year old code base in PHP/MySQL originally built for limited internal usage</li> <li>Some use of Laraval, but incomplete</li> <li>80-100 different UI screens, perhaps more</li> <li>A fairly complicated backend data aggregator that pulls information from remote sites for near real-time usage</li> <li>A growing customer base in the finance industry</li> </ul> <div>They are considering a re-build of the application.&nbsp; I hate re-builds - they are just always longer, harder than you think, and filled with peril.&nbsp; In particular, the ability for the organization to maintain the discipline a re-build requires for long enough to get it done seems to rarely happen - in my personal experience.&nbsp; In addition, there is the challenge of how much new development is done on the existing product while they wait for the new one, etc.&nbsp; In this case though, it seems to me that a re-build may be the only really viable solution.&nbsp;</div> <div><br> </div> <div>To this end, a few questions for this great group of folks:</div> <div><br> </div> <div>-- How do you convey and get the business to really understand what it will take to re-build a large complicated web application that has 10+ years of code, business logic, etc.?</div> <div><br> </div> <div>-- If you were going to re-build - basically build a new web application with a decent amount of financial data, what languages/dbs would you look to be using?</div> <div><br> </div> <div>-- Besides being a bit antiquated, I have stressed that recruiting developers for PHP work may be challenging, thoughts on this?&nbsp; Is this worth switching languages for? They have to hire new staff to do the re-build and it seems a bit short sighted to only look at PHP developers...</div> <div><br> </div> <div>-- In 2022, would you even consider building from a scratch a large complicated web app in PHP/Laraval?</div> <div><br> </div> <div>-- Would you prefer a "re-build while flying" or build it all new and rollout the new one separately approach?&nbsp; I like re-build while flying as it gets new code into production as soon as it is ready, but it definitely comes with compatibility challenges and ultimately might make the process even longer.<br> <br> Thanks for your thoughts.<br> <br> -Dan<br> <br> </div> <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>  </blockquote> </div>   <br><br><div style="max-width:590px;"><div><div style="font-size:small;  max-width:590px;  font-family:Arial,sans-serif;"><br></div><div style="max-width:590px;  font-family:Arial,sans-serif;  font-size:small;"></div></div><div><div><font color="#3333FF"><i></i></font></div></div></div></div>
          </div>
          <script>
            $('#quoted-204209180').on('show.bs.collapse', function () {
              $('#qlabel-204209180').text("Hide quoted text");
            })
            $('#quoted-204209180').on('hide.bs.collapse', function () {
              $('#qlabel-204209180').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204209180" aria-expanded="false" aria-controls="window-204209180"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204209180"><span id="likebutton204209180"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204209180, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204209180" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204209180">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:5799284"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204209180"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204209180"><span id="likestats204209180"></span></div>
        </div>
      </div>
      
        <div id="window-204209180" class="collapse">
          <form class="form" id="form204209180" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204209180" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204209180">
            <input type="hidden" id="groupname204209180" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204209180" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204209180" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204209180" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204209180">
    <textarea id="editor204209180" name="editor204209180" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204209180"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204209180"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204209180" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204209180" value="html">
              

              <div id="bccme204209180" class="checkbox">
                <label for="bccme204209180">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204209180" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204209180"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204209180" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204209180" name="preview" onclick="editor.PreviewMarkdown(204209180,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204209180" name="return" onclick="editor.ReturnMarkdown(204209180)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204209180" data-toggle="collapse" data-target="#window-204209180"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204209180" onclick="editor.TogglePrivate('204209180', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204209180" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204209180">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204209180">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204209180" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204209180&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204209180" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204209180">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204209180">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204209180" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204209180&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204209180').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204209180').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204209180", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204209180').tooltip()
            $('#showHistory204209180').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204209180, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204209180, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5185"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    David Subar
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 2:52pm">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5185"><span class="hidden-xs">#5185&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204212496">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div class="gmail_default" style="font-family:verdana,sans-serif;  color:#0000ff;">Re-build while flying takes longer but a build from scratch will always take longer than expected, have unexpected bugs, and will cause dissatisfaction of the executives who feel like they keep waiting and waiting to get back to where they were before. It is politically fraught. In addition, since the market changes the requirements for the new system will change as you are building it (assuming you are going for parity) so your ability to show value will be even further delayed. <br><br>There are some situations where you should build from scratch but I would generally suggest the strangle pattern as stated earlier by others. <br><br>Cornerstone OnDemand did a good job executing through this and I had the good fortune to interview one of their exec about it. If you want to listen, it is here"<br><br></div><blockquote><div class="gmail_default" style="font-family:verdana,sans-serif;  color:#0000ff;"><a href="https://www.interna.com/post/bottlenecks-team-topologies" rel="nofollow noopener" target="_blank">https://www.interna.com/post/bottlenecks-team-topologies</a> </div></blockquote><div class="gmail_default" style="font-family:verdana,sans-serif;  color:#0000ff;"><span class="sew8wsl12490rht"></span><span class="sew8wsl12490rht"></span><br>(The first 15 minutes address the monolith to microservices transformation and the next 45 take about org changes to facilitate the new architecture. Both are interesting.)<br><br>HTH,<br>David<br></div><div><div dir="ltr" class="gmail_signature"><div dir="ltr">-----------------<table><tbody><tr><td><p dir="ltr" style="margin-top:0pt;"><a href="http://interna.com/" target="_blank" rel="nofollow noopener"><span style="font-size:8pt;  font-family:Roboto,sans-serif;  background-color:transparent;  font-style:italic;"><span style="display:inline-block;  width:84px;"><img src="https://lh6.googleusercontent.com/BbEV4BXcJ4XXYifPSzoTJtFfXwaZmPl3sd8Ly6g-V71vdhB1J72oUVHIWbRJfhaYQavdeWdgbvbt1RSSgySt_BQVZc39JVAbHVX5wzryRv4RAXFnmhZeCaSXg-coASIHdY8DV9U1" width="84" height="61" style="margin-left:0px;  margin-top:0px;" class="myimg-responsive"></span></span></a></p></td><td><p dir="ltr" style="margin-top:0pt;"><span style="font-size:13pt;  font-family:Roboto,sans-serif;  color:rgb(255,120,2);  background-color:transparent;  font-weight:700;">David Subar</span></p><p dir="ltr" style="margin-top:0pt;"><span style="font-size:11pt;  font-family:Roboto,sans-serif;  color:rgb(68,55,66);  background-color:transparent;">Founder and Managing Partner</span></p><p dir="ltr" style="margin-top:0pt;"><a href="http://www.interna.com/" target="_blank" rel="nofollow noopener"><span style="font-size:11pt;  font-family:Roboto,sans-serif;  color:rgb(25,100,126);  background-color:transparent;">Website</span></a><span style="font-size:11pt;  font-family:Roboto,sans-serif;  color:rgb(25,100,126);  background-color:transparent;"> | </span><a href="http://linkedin.com/in/davidsubar" target="_blank" rel="nofollow noopener"><span style="font-size:11pt;  font-family:Roboto,sans-serif;  color:rgb(25,100,126);  background-color:transparent;">LinkedIn</span></a><span style="font-size:11pt;  font-family:Roboto,sans-serif;  color:rgb(25,100,126);  background-color:transparent;"> | </span><a href="http://twitter.com/dsubar" target="_blank" rel="nofollow noopener"><span style="font-size:11pt;  font-family:Roboto,sans-serif;  color:rgb(25,100,126);  background-color:transparent;">Twitter</span></a></p></td></tr></tbody></table></div></div></div><br></div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 1:39 PM Ghazenfer Mansoor &lt;<a href="mailto:gmansoor@technologyrivers.com" rel="nofollow noopener" target="_blank">gmansoor@technologyrivers.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div dir="ltr">Dan,&nbsp;<div>In addition to the problems you mentioned, do you also have a problem with the current state of the application, or is it quite stable? I prefer "re-build while flying" because you can gradually build instead of building a brand new system with tons of new features that may also take a long time to build, and then migrate.&nbsp; In my experience, "re-build while flying" keeps users engaged and has a better outcome from business perspectives.&nbsp;I would build a new front-end with a combination of new and existing API, maybe proxy/delegate in some cases, <span>especially</span>&nbsp;for new modules.</div><div><br></div><div><div dir="ltr"><div><div><div style="font-family:arial,sans-serif;  font-size:13px;"><span style="font-family:Arial,sans-serif;">Ghazenfer Mansoor</span></div><div dir="ltr" style="font-family:arial,sans-serif;  font-size:13px;"><div><div><div><div style="max-width:590px;  font-family:Arial,sans-serif;"><div dir="ltr"><div><div><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr"><div dir="ltr">(W):&nbsp;703.444.0505 x 101&nbsp;<br><a href="mailto:gmansoor@technologyrivers.com" target="_blank" rel="nofollow noopener">gmansoor@technologyrivers.com</a><br><a href="https://www.linkedin.com/in/gmansoor/" target="_blank" rel="nofollow noopener">LinkedIn</a>&nbsp;|&nbsp;&nbsp;<a href="https://www.facebook.com/gmansoor" target="_blank" rel="nofollow noopener">Facebook</a>&nbsp;|&nbsp;<a href="https://twitter.com/gmansoor" target="_blank" rel="nofollow noopener">Twitter</a>&nbsp;|&nbsp;&nbsp;<a href="https://www.instagram.com/techrivers/" target="_blank" rel="nofollow noopener">Instagram</a><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener"></a>&nbsp;|&nbsp;<a href="https://medium.com/@gmansoor" target="_blank" rel="nofollow noopener">Medium</a>&nbsp;</div><div dir="ltr"><br>Technology Rivers LLC:</div><div dir="ltr"><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener">Web</a>&nbsp;|&nbsp;<a href="https://www.linkedin.com/company/technology-rivers-llc/" target="_blank" rel="nofollow noopener">LinkedIn</a>&nbsp;|&nbsp;<a href="https://www.instagram.com/techrivers/" target="_blank" rel="nofollow noopener">Instagram</a><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener"></a>&nbsp;|&nbsp;<a href="https://twitter.com/techrivers" target="_blank" rel="nofollow noopener">Twitter</a>&nbsp;|&nbsp;&nbsp;<a href="https://www.facebook.com/techrivers" target="_blank" rel="nofollow noopener">Facebook</a>&nbsp;<a href="https://medium.com/@gmansoor" target="_blank" rel="nofollow noopener"></a>|&nbsp;<a href="https://www.youtube.com/channel/UCqU2dUudlTP1djS9zxAsYIw/" target="_blank" rel="nofollow noopener">YouTube</a>&nbsp;|&nbsp;<a href="https://technologyrivers.com/reviews" target="_blank" rel="nofollow noopener">Reviews</a>&nbsp;|&nbsp;<a href="https://technologyrivers.com/our-work" target="_blank" rel="nofollow noopener">Our Work</a></div><div dir="ltr"><br></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div></div><div><div><div style="max-width:590px;  font-family:Arial,sans-serif;"></div></div><div><div><font color="#3333FF"><i></i></font></div></div></div></div></div></div></div><img align="left" width="0" height="0" style=" width: 0px;" src="https://technologyrivers.mxspruce.com/api/track/v2/DBJruJdPmmmthgJLf/gIt92YuMnclZXayl3Zvx2buh2YlRHQy92bz5WYtdmI/Iybp5ycwV3bydmLzVGaj5Wds9GdjBUZkl2dkxmcvdnI/ISZkl2dkxmcvdnI?sc=false" alt="" class="myimg-responsive"> <div style="max-width:590px;"> <p><br></p> <div class="gmail_extra"> <p><br></p> <div class="gmail_quote"> On Tue, Apr 26, 2022 at 11:27 AM Dan Richards <span dir="ltr"> &lt;<a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>&gt;</span> wrote:<br> <blockquote class="gmail_quote"> <u></u> <div>I have a client I've been consulting with for a couple years.&nbsp; They are not a software company, but they have ended up in the software business by building an internal application and then they eventually started selling it to clients and now they have:</div> <ul> <li>A 10+ year old code base in PHP/MySQL originally built for limited internal usage</li> <li>Some use of Laraval, but incomplete</li> <li>80-100 different UI screens, perhaps more</li> <li>A fairly complicated backend data aggregator that pulls information from remote sites for near real-time usage</li> <li>A growing customer base in the finance industry</li> </ul> <div>They are considering a re-build of the application.&nbsp; I hate re-builds - they are just always longer, harder than you think, and filled with peril.&nbsp; In particular, the ability for the organization to maintain the discipline a re-build requires for long enough to get it done seems to rarely happen - in my personal experience.&nbsp; In addition, there is the challenge of how much new development is done on the existing product while they wait for the new one, etc.&nbsp; In this case though, it seems to me that a re-build may be the only really viable solution.&nbsp;</div> <div><br> </div> <div>To this end, a few questions for this great group of folks:</div> <div><br> </div> <div>-- How do you convey and get the business to really understand what it will take to re-build a large complicated web application that has 10+ years of code, business logic, etc.?</div> <div><br> </div> <div>-- If you were going to re-build - basically build a new web application with a decent amount of financial data, what languages/dbs would you look to be using?</div> <div><br> </div> <div>-- Besides being a bit antiquated, I have stressed that recruiting developers for PHP work may be challenging, thoughts on this?&nbsp; Is this worth switching languages for? They have to hire new staff to do the re-build and it seems a bit short sighted to only look at PHP developers...</div> <div><br> </div> <div>-- In 2022, would you even consider building from a scratch a large complicated web app in PHP/Laraval?</div> <div><br> </div> <div>-- Would you prefer a "re-build while flying" or build it all new and rollout the new one separately approach?&nbsp; I like re-build while flying as it gets new code into production as soon as it is ready, but it definitely comes with compatibility challenges and ultimately might make the process even longer.<br> <br> Thanks for your thoughts.<br> <br> -Dan<br> <br> </div> <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>  </blockquote> </div> </div> </div> <br><br><div style="max-width:590px;"><div><div style="font-size:small;  max-width:590px;  font-family:Arial,sans-serif;"><br></div><div style="max-width:590px;  font-family:Arial,sans-serif;  font-size:small;"></div></div><div><div><font color="#3333FF"><i></i></font></div></div></div> 


  

<p></p><p></p></blockquote></div></div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204212496" aria-expanded="false" aria-controls="window-204212496"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204212496"><span id="likebutton204212496"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204212496, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204212496" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204212496">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:5837507"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204212496"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204212496"><span id="likestats204212496"></span></div>
        </div>
      </div>
      
        <div id="window-204212496" class="collapse">
          <form class="form" id="form204212496" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204212496" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204212496">
            <input type="hidden" id="groupname204212496" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204212496" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204212496" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204212496" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204212496">
    <textarea id="editor204212496" name="editor204212496" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204212496"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204212496"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204212496" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204212496" value="html">
              

              <div id="bccme204212496" class="checkbox">
                <label for="bccme204212496">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204212496" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204212496"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204212496" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204212496" name="preview" onclick="editor.PreviewMarkdown(204212496,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204212496" name="return" onclick="editor.ReturnMarkdown(204212496)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204212496" data-toggle="collapse" data-target="#window-204212496"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204212496" onclick="editor.TogglePrivate('204212496', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204212496" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204212496">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204212496">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204212496" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204212496&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204212496" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204212496">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204212496">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204212496" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204212496&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204212496').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204212496').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204212496", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204212496').tooltip()
            $('#showHistory204212496').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204212496, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204212496, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5186"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    andy.pai
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 26, 2022 3:35pm">Apr 26</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5186"><span class="hidden-xs">#5186&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204214264">
        <div class="forcebreak" dir="auto"><div dir="ltr">Dan,<div>I just wanted to add a comment on staffing a project like this. I've only ever seen this go well when you start it off with a small team of maybe 1-3 very experienced engineers,&nbsp;and let them be focused on the work. Treat it like a startup would and let a small, very talented team do one thing and do it well, and you'll be surprised how fast they can move.</div><div><br></div><div>Trying to migrate a lot of features to a new architecture with less experienced folks, or trying to do this alongside of maintaining/extending the existing product, or trying to tackle the early stages of a large green field project with a big team are all super hard, and the project will take many times longer than you think.&nbsp;&nbsp;</div><div><br></div><div>Hopefully the data aggregation piece you mentioned is separate enough that you can set that aside and only address the web app. If not, maybe splitting that out would be a good first step.</div><div><br></div><div>Andy&nbsp;</div></div><br></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204214264" role="button" data-toggle="collapse" href="#quoted-204214264" aria-expanded="false" aria-controls="quoted-204214264"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204214264" class="collapse forcebreak">
            <div dir="auto"><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Tue, Apr 26, 2022 at 9:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" rel="nofollow noopener" target="_blank">rodan@stradscon.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">
  

    
  
  <div>
    <div>I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul>
      <li>A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li>Some use of Laraval, but incomplete</li>
      <li>80-100 different UI screens, perhaps more</li>
      <li>A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li>A growing customer base in the finance industry</li>
    </ul>
    <div>They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div><br>
    </div>
    <div>To this end, a few questions for this great group of folks:</div>
    <div><br>
    </div>
    <div>-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div><br>
    </div>
    <div>-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div><br>
    </div>
    <div>-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div><br>
    </div>
    <div>-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div><br>
    </div>
    <div>-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre>-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre>
  </div>



  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204214264').on('show.bs.collapse', function () {
              $('#qlabel-204214264').text("Hide quoted text");
            })
            $('#quoted-204214264').on('hide.bs.collapse', function () {
              $('#qlabel-204214264').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204214264" aria-expanded="false" aria-controls="window-204214264"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204214264"><span id="likebutton204214264"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204214264, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204214264" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204214264">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388149"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204214264"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204214264"><span id="likestats204214264"></span></div>
        </div>
      </div>
      
        <div id="window-204214264" class="collapse">
          <form class="form" id="form204214264" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204214264" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204214264">
            <input type="hidden" id="groupname204214264" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204214264" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204214264" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204214264" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204214264">
    <textarea id="editor204214264" name="editor204214264" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204214264"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204214264"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204214264" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204214264" value="html">
              

              <div id="bccme204214264" class="checkbox">
                <label for="bccme204214264">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204214264" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204214264"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204214264" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204214264" name="preview" onclick="editor.PreviewMarkdown(204214264,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204214264" name="return" onclick="editor.ReturnMarkdown(204214264)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204214264" data-toggle="collapse" data-target="#window-204214264"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204214264" onclick="editor.TogglePrivate('204214264', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204214264" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204214264">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204214264">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204214264" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204214264&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204214264" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204214264">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204214264">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204214264" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204214264&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204214264').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204214264').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204214264", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204214264').tooltip()
            $('#showHistory204214264').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204214264, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204214264, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5195"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <img src="https://ctolunches.groups.io/g/worldwide/profilephoto/3859741" width="40" height="40" class="img-rounded">
    
    
  
	
    Dominic Tancredi
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 8:34am">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5195"><span class="hidden-xs">#5195&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204296745">
        <div class="forcebreak" dir="auto"><div><div><div><div>The only (dissenting-and-biased) opinion I have is that PHP/Laravel can be a solid choice. Everyone, myself included, loves Next.js (and Nuxt.js) and there's a place for React/Redux/etc. for true web applications but they all need deep customizations.<br></div><div><br></div><div>The modern&nbsp;stack we recommend (and includes robust applications for Enterprise/MidMarket/Startup) engagements is called <a href="https://tallstack.dev/" target="_blank" rel="nofollow noopener">"TALL"-stack</a>&nbsp;<a href="https://tallstack.dev/" target="_blank" rel="nofollow noopener">(T</a><span><a href="https://tallstack.dev/" target="_blank" rel="nofollow noopener">ailwind, Alpine, Laravel, Livewire</a></span><a href="https://tallstack.dev/" target="_blank" rel="nofollow noopener">)</a>. Taylor and his team has done a solid job with <a href="https://nova.laravel.com/" target="_blank" rel="nofollow noopener">Nova</a>&nbsp;(admin panel) and <a href="https://filamentphp.com/" target="_blank" rel="nofollow noopener">Filament</a>&nbsp;(components), and there's a lot of polished work done. The alternative would be "VILT" stack which is Vue + <a href="https://inertiajs.com/" target="_blank" rel="nofollow noopener">Intertia</a> + Laravel + Tailwind but I think it's a little too new.<br></div><div><br></div><div>I've never been impressed with Django but Atom and Flask are solid. Ruby on Rails is… just so fun to configure and manage over 10+ years. .NET has powerful&nbsp;but you have to enjoy drinking Kool-Aid.&nbsp;<br></div><div><br></div><div>PHP developers are now 20+ years older, more mature, aware of patterns, etc. It's like seeing Nirvana or Green Day play at Carnegie - you're going to get a more solid experience than the o.g. days. but it still retains the punk rock roots.&nbsp;<br></div><div><br></div><div><br></div></div><div><div style="display: none;   width: 0px;"></div><br><div class="gmail_signature"><div><div dir="ltr"><div>Best,<br></div><div>Dom</div><div><br><table class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size"><tbody class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size"><tr class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size"><td colspan="1" rowspan="1" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size"><img height="96" width="96" style="background-color:rgb(242,97,30);  max-width:85px;" title="" src="https://dtsignaturegen.netlify.app/img/dt-logo-full.568645e1.png" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size myimg-responsive"></td><td colspan="1" rowspan="1" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size"><div style="margin-left:5px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size"><p style="font-weight:700;  font-size:16px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height">Dom Tancredi</p><p style="font-size:11px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height">CoFounder</p><div style="width:50px;  margin-top:5px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size"></div><p style="font-weight:700;  font-size:12px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height">MAKE. PROGRESS.</p><p style="font-size:11px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height">Office: 773.377.5585&nbsp;<span style="margin-left:3px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height">| Mobile: 718.431.5137</span></p><p style="font-size:11px;" class="sh-preserve-color sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height"><span style="" class="sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height"><a href="mailto:dom@domandtom.com" target="_blank" class="sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height" rel="nofollow noopener">dom@domandtom.com</a> |</span><a href="http://domandtom.com" target="_blank" class="sh-preserve-font-family sh-preserve-font-size sh-preserve-line-height" rel="nofollow noopener">domandtom.com</a></p></div></td></tr></tbody></table></div></div></div><br><div style="">Sent via <a href="https://sprh.mn/?vip=dom@domandtom.com" target="_blank" rel="nofollow noopener">Superhuman</a></div><br></div></div><br></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204296745" role="button" data-toggle="collapse" href="#quoted-204296745" aria-expanded="false" aria-controls="quoted-204296745"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204296745" class="collapse forcebreak">
            <div dir="auto"><div><div class="gmail_quote">On Tue, Apr 26, 2022 at 6:35 PM, andy.pai <span dir="ltr">&lt;<a href="mailto:andy.pai@gmail.com" target="_blank" rel="nofollow noopener">andy.pai@gmail.com</a>&gt;</span> wrote:<br><blockquote class="gmail_quote"><div class="gmail_extra"><div class="gmail_quote sh-color-black sh-color" style="" id="null"><div dir="ltr" class="sh-color-black sh-color">Dan,<div class="sh-color-black sh-color">I just wanted to add a comment on staffing a project like this. I've only ever seen this go well when you start it off with a small team of maybe 1-3 very experienced engineers,&nbsp;and let them be focused on the work. Treat it like a startup would and let a small, very talented team do one thing and do it well, and you'll be surprised how fast they can move.</div><div class="sh-color-black sh-color"><br></div><div class="sh-color-black sh-color">Trying to migrate a lot of features to a new architecture with less experienced folks, or trying to do this alongside of maintaining/extending the existing product, or trying to tackle the early stages of a large green field project with a big team are all super hard, and the project will take many times longer than you think.&nbsp;&nbsp;</div><div class="sh-color-black sh-color"><br></div><div class="sh-color-black sh-color">Hopefully the data aggregation piece you mentioned is separate enough that you can set that aside and only address the web app. If not, maybe splitting that out would be a good first step.</div><div class="sh-color-black sh-color"><br></div><div class="sh-color-black sh-color">Andy&nbsp;</div></div><br><div class="gmail_quote sh-color-black sh-color"><div class="gmail_attr sh-color-black sh-color" dir="ltr">On Tue, Apr 26, 2022 at 9:27 AM Dan Richards &lt;<a href="mailto:rodan@stradscon.com" target="_blank" class="sh-color-blue sh-color" rel="nofollow noopener">rodan@<wbr>stradscon.<wbr>com</a>&gt; wrote:<br></div><blockquote class="gmail_quote sh-color-black sh-color">
  

    
  
  <div class="sh-color-black sh-color">
    <div class="sh-color-black sh-color">I have a client
      I've been consulting with for a couple years.&nbsp; They are not a
      software company, but they have ended up in the software business
      by building an internal application and then they eventually
      started selling it to clients and now they have:</div>
    <ul class="sh-color-black sh-color">
      <li class="sh-color-black sh-color">A 10+ year old code base in PHP/MySQL originally built for
        limited internal usage</li>
      <li class="sh-color-black sh-color">Some use of Laraval, but incomplete</li>
      <li class="sh-color-black sh-color">80-100 different UI screens, perhaps more</li>
      <li class="sh-color-black sh-color">A fairly complicated backend data aggregator that pulls
        information from remote sites for near real-time usage</li>
      <li class="sh-color-black sh-color">A growing customer base in the finance industry</li>
    </ul>
    <div class="sh-color-black sh-color">They are considering a re-build of the application.&nbsp; I hate
      re-builds - they are just always longer, harder than you think,
      and filled with peril.&nbsp; In particular, the ability for the
      organization to maintain the discipline a re-build requires for
      long enough to get it done seems to rarely happen - in my personal
      experience.&nbsp; In addition, there is the challenge of how much new
      development is done on the existing product while they wait for
      the new one, etc.&nbsp; In this case though, it seems to me that a
      re-build may be the only really viable solution.&nbsp; </div>
    <div class="sh-color-black sh-color"><br>
    </div>
    <div class="sh-color-black sh-color">To this end, a few questions for this great group of folks:</div>
    <div class="sh-color-black sh-color"><br>
    </div>
    <div class="sh-color-black sh-color">-- How do you convey and get the business to really understand
      what it will take to re-build a large complicated web application
      that has 10+ years of code, business logic, etc.?</div>
    <div class="sh-color-black sh-color"><br>
    </div>
    <div class="sh-color-black sh-color">-- If you were going to re-build - basically build a new web
      application with a decent amount of financial data, what
      languages/dbs would you look to be using?</div>
    <div class="sh-color-black sh-color"><br>
    </div>
    <div class="sh-color-black sh-color">-- Besides being a bit antiquated, I have stressed that
      recruiting developers for PHP work may be challenging, thoughts on
      this?&nbsp; Is this worth switching languages for? They have to hire
      new staff to do the re-build and it seems a bit short sighted to
      only look at PHP developers...</div>
    <div class="sh-color-black sh-color"><br>
    </div>
    <div class="sh-color-black sh-color">-- In 2022, would you even consider building from a scratch a
      large complicated web app in PHP/Laraval?</div>
    <div class="sh-color-black sh-color"><br>
    </div>
    <div class="sh-color-black sh-color">-- Would you prefer a "re-build while flying" or build it all
      new and rollout the new one separately approach?&nbsp; I like re-build
      while flying as it gets new code into production as soon as it is
      ready, but it definitely comes with compatibility challenges and
      ultimately might make the process even longer.<br>
      <br>
      Thanks for your thoughts.<br>
      <br>
      -Dan<br>
      <br>
    </div>
    <pre class="sh-color-black sh-color">-- 
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" class="sh-color-blue sh-color" rel="nofollow noopener">rodan@<wbr>stradscon.<wbr>com</a>
t: @rodandar</pre>
  </div>



  

<p class="sh-color-black sh-color"></p><p class="sh-color-black sh-color"></p></blockquote></div>


 </div></div></blockquote></div></div><br></div>
          </div>
          <script>
            $('#quoted-204296745').on('show.bs.collapse', function () {
              $('#qlabel-204296745').text("Hide quoted text");
            })
            $('#quoted-204296745').on('hide.bs.collapse', function () {
              $('#qlabel-204296745').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204296745" aria-expanded="false" aria-controls="window-204296745"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204296745"><span id="likebutton204296745"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204296745, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204296745" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204296745">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1766614"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204296745"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204296745"><span id="likestats204296745"></span></div>
        </div>
      </div>
      
        <div id="window-204296745" class="collapse">
          <form class="form" id="form204296745" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204296745" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204296745">
            <input type="hidden" id="groupname204296745" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204296745" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204296745" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204296745" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204296745">
    <textarea id="editor204296745" name="editor204296745" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204296745"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204296745"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204296745" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204296745" value="html">
              

              <div id="bccme204296745" class="checkbox">
                <label for="bccme204296745">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204296745" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204296745"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204296745" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204296745" name="preview" onclick="editor.PreviewMarkdown(204296745,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204296745" name="return" onclick="editor.ReturnMarkdown(204296745)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204296745" data-toggle="collapse" data-target="#window-204296745"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204296745" onclick="editor.TogglePrivate('204296745', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204296745" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204296745">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204296745">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204296745" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204296745&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204296745" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204296745">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204296745">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204296745" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204296745&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204296745').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204296745').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204296745", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204296745').tooltip()
            $('#showHistory204296745').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204296745, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204296745, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5197"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Ryan Vice
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 9:20am">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5197"><span class="hidden-xs">#5197&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204299497">
        <div class="forcebreak" dir="auto"><div>
<div>Adding onto Dan’s point. I haven’t done it but I’ve been told from respected CTOs that this is a great use case for GraphQL. If you put a GraphQL API over the old API then you can provide a lot of flexibility to the new UI.</div>
</div>
<div><br>
<table>
<tbody>
<tr>
<td valign="top" rowspan="6" align="center"><img alt="photograph" width="132" src="https://i.ibb.co/n7jqV86/ryan-vice-headshot.jpg" style="width:132px;" class="myimg-responsive"></td>
<td>
<table>
<tbody>
<tr>
<td valign="top"><span style="font-weight:700;"><span style="font-size:14pt;  color:rgb(106,55,143);">Ryan Vice<br></span></span><span style="font-size:10pt;  color:rgb(68,68,68);">CEO</span>&nbsp;<span style="font-size:10pt;  color:rgb(68,68,68);">|&nbsp;</span><span style="font-size:10pt;  color:rgb(68,68,68);">Vice Software, LLC</span></td>
</tr>
<tr>
<td valign="top"><span style="color:rgb(106,55,143);"><span style="font-weight:700;">m:</span></span><span style="font-size:10pt;">&nbsp;5127881126<br></span><span style="color:rgb(106,55,143);"><span style="font-weight:700;">p:</span></span><span style="font-size:10pt;">&nbsp;1 (855) 349-2248<br></span><span style="color:rgb(106,55,143);"><span style="font-weight:700;">e:</span></span><span style="font-size:10pt;">&nbsp;<a href="mailto:ryan@vicesoftware.com" target="_blank" rel="nofollow noopener">ryan@vicesoftware.com</a></span></td>
</tr>
<tr>
<td valign="top"><span style="font-size:10pt;  color:rgb(106,55,143);">10614 Sans Souci PL<br></span><span style="font-size:10pt;  color:rgb(106,55,143);">Austin, TX 78759</span></td>
</tr>
<tr>
<td valign="top"><a href="http://www.vicesoftware.com/" target="_blank" rel="nofollow noopener"><span style="font-size:10pt;  color:rgb(245,130,30);">www.vicesoftware.com</span></a></td>
</tr>
<tr>
<td valign="top"><a href="https://www.facebook.com/ViceSoftware/" target="_blank" rel="nofollow noopener"><img width="23" alt="facebook icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator/simplephoto/fb.png" style="width:23px;" class="myimg-responsive"></a>&nbsp;<a href="https://twitter.com/RyanVice1" target="_blank" rel="nofollow noopener"><img width="23" alt="twitter icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator/simplephoto/tt.png" style="width:23px;" class="myimg-responsive"></a>&nbsp;<a href="https://www.youtube.com/channel/UCEwukAl1aCFqb_RhnbgM9cw" target="_blank" rel="nofollow noopener"><img width="23" alt="youtube icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator/simplephoto/yt.png" style="width:23px;" class="myimg-responsive"></a>&nbsp;<a href="https://www.linkedin.com/company/vice-software-llc" target="_blank" rel="nofollow noopener"><img width="23" alt="linkedin icon" src="https://codetwocdn.azureedge.net/images/mail-signatures/generator/simplephoto/ln.png" style="width:23px;" class="myimg-responsive"></a>&nbsp;</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204299497" role="button" data-toggle="collapse" href="#quoted-204299497" aria-expanded="false" aria-controls="quoted-204299497"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204299497" class="collapse forcebreak">
            <div dir="auto"><div>On Apr 26, 2022, 3:39 PM -0500, Ghazenfer Mansoor &lt;gmansoor@technologyrivers.com&gt;, wrote:<br>
<blockquote>
<div dir="ltr">Dan,&nbsp;
<div>In addition to the problems you mentioned, do you also have a problem with the current state of the application, or is it quite stable? I prefer "re-build while flying" because you can gradually build instead of building a brand new system with tons of new features that may also take a long time to build, and then migrate.&nbsp; In my experience, "re-build while flying" keeps users engaged and has a better outcome from business perspectives.&nbsp;I would build a new front-end with a combination of new and existing API, maybe proxy/delegate in some cases, <span class="ng">especially</span>&nbsp;for new modules.</div>
<div><br></div>
<div>
<div dir="ltr">
<div>
<div>
<div style="font-family:arial,sans-serif;  font-size:13px;"><span style="font-family:Arial,sans-serif;">Ghazenfer Mansoor</span></div>
<div dir="ltr" style="font-family:arial,sans-serif;  font-size:13px;">
<div>
<div>
<div>
<div style="max-width:590px;  font-family:Arial,sans-serif;">
<div dir="ltr">
<div>
<div>
<div dir="ltr">
<div dir="ltr">
<div dir="ltr">
<div dir="ltr">
<div dir="ltr">
<div dir="ltr">
<div dir="ltr">
<div dir="ltr">
<div dir="ltr">(W):&nbsp;703.444.0505 x 101&nbsp;<br>
<a href="mailto:gmansoor@technologyrivers.com" target="_blank" rel="nofollow noopener">gmansoor@technologyrivers.com</a><br>
<a href="https://www.linkedin.com/in/gmansoor/" target="_blank" rel="nofollow noopener">LinkedIn</a>&nbsp;|&nbsp;&nbsp;<a href="https://www.facebook.com/gmansoor" target="_blank" rel="nofollow noopener">Facebook</a>&nbsp;|&nbsp;<a href="https://twitter.com/gmansoor" target="_blank" rel="nofollow noopener">Twitter</a><wbr>&nbsp;|&nbsp;&nbsp;<a href="https://www.instagram.com/techrivers/" target="_blank" rel="nofollow noopener">Instagram</a><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener"></a>&nbsp;|&nbsp;<a href="https://medium.com/@gmansoor" target="_blank" rel="nofollow noopener">Medium</a>&nbsp;</div>
<div dir="ltr"><br>
Technology Rivers LLC:</div>
<div dir="ltr"><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener">Web</a>&nbsp;|&nbsp;<a href="https://www.linkedin.com/company/technology-rivers-llc/" target="_blank" rel="nofollow noopener">LinkedIn</a>&nbsp;|&nbsp;<a href="https://www.instagram.com/techrivers/" target="_blank" rel="nofollow noopener">Instagram</a><a href="https://technologyrivers.com/" target="_blank" rel="nofollow noopener"></a>&nbsp;|&nbsp;<a href="https://twitter.com/techrivers" target="_blank" rel="nofollow noopener">T<wbr>witter</a>&nbsp;|&nbsp;&nbsp;<a href="https://www.facebook.com/techrivers" target="_blank" rel="nofollow noopener">Facebook</a>&nbsp;<a href="https://medium.com/@gmansoor" target="_blank" rel="nofollow noopener"></a>|&nbsp;<a href="https://www.youtube.com/channel/UCqU2dUudlTP1djS9zxAsYIw/" target="_blank" rel="nofollow noopener">YouTube</a>&nbsp;|<wbr>&nbsp;<a href="https://technologyrivers.com/reviews" target="_blank" rel="nofollow noopener">Reviews</a>&nbsp;|&nbsp;<a href="https://technologyrivers.com/our-work" target="_blank" rel="nofollow noopener">Our Work</a></div>
<div dir="ltr"><br></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div>
<div>
<div style="max-width:590px;  font-family:Arial,sans-serif;"></div>
</div>
<div>
<div><font color="#3333FF"><i></i></font></div>
</div>
</div>
</div>
</div>
</div>
</div>
<img align="left" width="0" height="0" style="width:0px;" src="https://technologyrivers.mxspruce.com/api/track/v2/DBJruJdPmmmthgJLf/gIt92YuMnclZXayl3Zvx2buh2YlRHQy92bz5WYtdmI/Iybp5ycwV3bydmLzVGaj5Wds9GdjBUZkl2dkxmcvdnI/ISZkl2dkxmcvdnI?sc=false" alt="" class="myimg-responsive">
<div style="max-width:590px;">
<p><br></p>
<div class="gmail_extra">
<p><br></p>
<div class="gmail_quote">On Tue, Apr 26, 2022 at 11:27 AM Dan Richards <span dir="ltr">&lt;<a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>&gt;</span> wrote:<br>
<blockquote class="gmail_quote"><u></u>
<div>I have a client I've been consulting with for a couple years.&nbsp; They are not a software company, but they have ended up in the software business by building an internal application and then they eventually started selling it to clients and now they have:</div>
<ul>
<li>A 10+ year old code base in PHP/MySQL originally built for limited internal usage</li>
<li>Some use of Laraval, but incomplete</li>
<li>80-100 different UI screens, perhaps more</li>
<li>A fairly complicated backend data aggregator that pulls information from remote sites for near real-time usage</li>
<li>A growing customer base in the finance industry</li>
</ul>
<div>They are considering a re-build of the application.&nbsp; I hate re-builds - they are just always longer, harder than you think, and filled with peril.&nbsp; In particular, the ability for the organization to maintain the discipline a re-build requires for long enough to get it done seems to rarely happen - in my personal experience.&nbsp; In addition, there is the challenge of how much new development is done on the existing product while they wait for the new one, etc.&nbsp; In this case though, it seems to me that a re-build may be the only really viable solution.&nbsp;</div>
<div><br></div>
<div>To this end, a few questions for this great group of folks:</div>
<div><br></div>
<div>-- How do you convey and get the business to really understand what it will take to re-build a large complicated web application that has 10+ years of code, business logic, etc.?</div>
<div><br></div>
<div>-- If you were going to re-build - basically build a new web application with a decent amount of financial data, what languages/dbs would you look to be using?</div>
<div><br></div>
<div>-- Besides being a bit antiquated, I have stressed that recruiting developers for PHP work may be challenging, thoughts on this?&nbsp; Is this worth switching languages for? They have to hire new staff to do the re-build and it seems a bit short sighted to only look at PHP developers...</div>
<div><br></div>
<div>-- In 2022, would you even consider building from a scratch a large complicated web app in PHP/Laraval?</div>
<div><br></div>
<div>-- Would you prefer a "re-build while flying" or build it all new and rollout the new one separately approach?&nbsp; I like re-build while flying as it gets new code into production as soon as it is ready, but it definitely comes with compatibility challenges and ultimately might make the process even longer.<br>
<br>
Thanks for your thoughts.<br>
<br>
-Dan<br>
<br></div>
<pre>--  
------------
Dan Richards
w: 617-249-4509
c: 617-388-0811
e: <a href="mailto:rodan@stradscon.com" target="_blank" rel="nofollow noopener">rodan@stradscon.com</a>
t: @rodandar</pre></blockquote>
</div>
</div>
</div>
<br>
<br>
<div style="max-width:590px;">
<div>
<div style="font-size:small;  max-width:590px;  font-family:Arial,sans-serif;"><br></div>
<div style="max-width:590px;  font-family:Arial,sans-serif;  font-size:small;"></div>
</div>
<div>
<div><font color="#3333FF"><i></i></font></div>
</div>
</div>

</blockquote>
</div>

</div>
          </div>
          <script>
            $('#quoted-204299497').on('show.bs.collapse', function () {
              $('#qlabel-204299497').text("Hide quoted text");
            })
            $('#quoted-204299497').on('hide.bs.collapse', function () {
              $('#qlabel-204299497').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204299497" aria-expanded="false" aria-controls="window-204299497"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204299497"><span id="likebutton204299497"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204299497, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204299497" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204299497">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1443309"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204299497"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204299497"><span id="likestats204299497"></span></div>
        </div>
      </div>
      
        <div id="window-204299497" class="collapse">
          <form class="form" id="form204299497" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204299497" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204299497">
            <input type="hidden" id="groupname204299497" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204299497" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204299497" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204299497" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204299497">
    <textarea id="editor204299497" name="editor204299497" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204299497"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204299497"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204299497" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204299497" value="html">
              

              <div id="bccme204299497" class="checkbox">
                <label for="bccme204299497">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204299497" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204299497"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204299497" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204299497" name="preview" onclick="editor.PreviewMarkdown(204299497,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204299497" name="return" onclick="editor.ReturnMarkdown(204299497)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204299497" data-toggle="collapse" data-target="#window-204299497"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204299497" onclick="editor.TogglePrivate('204299497', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204299497" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204299497">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204299497">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204299497" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204299497&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204299497" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204299497">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204299497">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204299497" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204299497&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204299497').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204299497').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204299497", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204299497').tooltip()
            $('#showHistory204299497').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204299497, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204299497, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5198"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Josiah Haswell
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 11:01am">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5198"><span class="hidden-xs">#5198&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204304961">
        <div class="forcebreak" dir="auto">I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!</div>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204304961" aria-expanded="false" aria-controls="window-204304961"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204304961"><span id="likebutton204304961"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204304961, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204304961" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204304961">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1681689"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204304961"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204304961"><span id="likestats204304961"></span></div>
        </div>
      </div>
      
        <div id="window-204304961" class="collapse">
          <form class="form" id="form204304961" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204304961" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204304961">
            <input type="hidden" id="groupname204304961" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204304961" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204304961" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204304961" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204304961">
    <textarea id="editor204304961" name="editor204304961" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204304961"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204304961"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204304961" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204304961" value="html">
              

              <div id="bccme204304961" class="checkbox">
                <label for="bccme204304961">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204304961" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204304961"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204304961" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204304961" name="preview" onclick="editor.PreviewMarkdown(204304961,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204304961" name="return" onclick="editor.ReturnMarkdown(204304961)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204304961" data-toggle="collapse" data-target="#window-204304961"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204304961" onclick="editor.TogglePrivate('204304961', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204304961" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204304961">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204304961">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204304961" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204304961&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204304961" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204304961">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204304961">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204304961" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204304961&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204304961').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204304961').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204304961", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204304961').tooltip()
            $('#showHistory204304961').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204304961, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204304961, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5199"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Erik Brandsberg
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 11:54am">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5199"><span class="hidden-xs">#5199&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204307662">
        <div class="forcebreak" dir="auto"><div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well, as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204307662" role="button" data-toggle="collapse" href="#quoted-204307662" aria-expanded="false" aria-controls="quoted-204307662"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204307662" class="collapse forcebreak">
            <div dir="auto"><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" rel="nofollow noopener" target="_blank">josiah@sunshower.io</a>&gt; wrote:<br></div><blockquote class="gmail_quote">I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!


  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204307662').on('show.bs.collapse', function () {
              $('#qlabel-204307662').text("Hide quoted text");
            })
            $('#quoted-204307662').on('hide.bs.collapse', function () {
              $('#qlabel-204307662').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204307662" aria-expanded="false" aria-controls="window-204307662"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204307662"><span id="likebutton204307662"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204307662, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204307662" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204307662">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:4507539"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204307662"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204307662"><span id="likestats204307662"></span></div>
        </div>
      </div>
      
        <div id="window-204307662" class="collapse">
          <form class="form" id="form204307662" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204307662" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204307662">
            <input type="hidden" id="groupname204307662" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204307662" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204307662" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204307662" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204307662">
    <textarea id="editor204307662" name="editor204307662" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204307662"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204307662"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204307662" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204307662" value="html">
              

              <div id="bccme204307662" class="checkbox">
                <label for="bccme204307662">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204307662" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204307662"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204307662" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204307662" name="preview" onclick="editor.PreviewMarkdown(204307662,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204307662" name="return" onclick="editor.ReturnMarkdown(204307662)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204307662" data-toggle="collapse" data-target="#window-204307662"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204307662" onclick="editor.TogglePrivate('204307662', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204307662" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204307662">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204307662">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204307662" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204307662&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204307662" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204307662">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204307662">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204307662" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204307662&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204307662').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204307662').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204307662", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204307662').tooltip()
            $('#showHistory204307662').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204307662, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204307662, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5200"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    james Ford
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 2:19pm">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5200"><span class="hidden-xs">#5200&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204314762">
        <div class="forcebreak" dir="auto"><meta http-equiv="content-type">Been a lot of great ideas, patterns and suggestions….<div><br></div><div>In the end I think it’s always the same…. Find the seams, encapsulate the ugliness, isolate it behind an interface and evolve the service behind the interface….</div><div><br></div><div><br><br><div dir="ltr"><br><div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><span style="background-color: rgba(255, 255, 255, 0);">--&nbsp;<br></span><div class="m_7017788891221011597gmail_signature"><div dir="ltr"><i>James Ford</i><div><span style="background-color: rgba(255, 255, 255, 0);">Founder</span></div><div><span style="background-color: rgba(255, 255, 255, 0);">Pareidolia, LLC</span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><u>https://www.pareidolia.rocks</u></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br>"Where Vision meets Reality"</span></div></div></div></div></div><div dir="ltr"><br></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204314762" role="button" data-toggle="collapse" href="#quoted-204314762" aria-expanded="false" aria-controls="quoted-204314762"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204314762" class="collapse forcebreak">
            <div dir="auto"><blockquote>On Apr 28, 2022, at 2:54 PM, Erik Brandsberg &lt;erik@heimdalldata.com&gt; wrote:<br><br></blockquote><blockquote><div dir="ltr">﻿<div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well, as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" rel="nofollow noopener" target="_blank">josiah@sunshower.io</a>&gt; wrote:<br></div><blockquote class="gmail_quote">I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!


  

<p></p><p></p></blockquote></div>


  

</div></blockquote></div>
          </div>
          <script>
            $('#quoted-204314762').on('show.bs.collapse', function () {
              $('#qlabel-204314762').text("Hide quoted text");
            })
            $('#quoted-204314762').on('hide.bs.collapse', function () {
              $('#qlabel-204314762').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204314762" aria-expanded="false" aria-controls="window-204314762"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204314762"><span id="likebutton204314762"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204314762, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204314762" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204314762">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1615858"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204314762"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204314762"><span id="likestats204314762"></span></div>
        </div>
      </div>
      
        <div id="window-204314762" class="collapse">
          <form class="form" id="form204314762" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204314762" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204314762">
            <input type="hidden" id="groupname204314762" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204314762" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204314762" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204314762" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204314762">
    <textarea id="editor204314762" name="editor204314762" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204314762"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204314762"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204314762" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204314762" value="html">
              

              <div id="bccme204314762" class="checkbox">
                <label for="bccme204314762">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204314762" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204314762"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204314762" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204314762" name="preview" onclick="editor.PreviewMarkdown(204314762,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204314762" name="return" onclick="editor.ReturnMarkdown(204314762)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204314762" data-toggle="collapse" data-target="#window-204314762"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204314762" onclick="editor.TogglePrivate('204314762', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204314762" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204314762">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204314762">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204314762" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204314762&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204314762" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204314762">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204314762">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204314762" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204314762&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204314762').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204314762').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204314762", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204314762').tooltip()
            $('#showHistory204314762').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204314762, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204314762, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5201"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    james Ford
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 2:27pm">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5201"><span class="hidden-xs">#5201&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204315170">
        <div class="forcebreak" dir="auto"><meta http-equiv="content-type">At ADP we had a cobol mainframe payroll processing Engine that was 40 years old…. Full rewrites of old systems bring along obsoleted functionality unless you can get the telemetry to know what is used and what is no longer needed. &nbsp;I<br><br><div dir="ltr"><br><div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><span style="background-color: rgba(255, 255, 255, 0);">--&nbsp;<br></span><div class="m_7017788891221011597gmail_signature"><div dir="ltr"><i>James Ford</i><div><span style="background-color: rgba(255, 255, 255, 0);">Founder</span></div><div><span style="background-color: rgba(255, 255, 255, 0);">Pareidolia, LLC</span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><u>https://www.pareidolia.rocks</u></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br>"Where Vision meets Reality"</span></div></div></div></div></div><div dir="ltr"><br></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204315170" role="button" data-toggle="collapse" href="#quoted-204315170" aria-expanded="false" aria-controls="quoted-204315170"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204315170" class="collapse forcebreak">
            <div dir="auto"><blockquote>On Apr 28, 2022, at 5:19 PM, james Ford via groups.io &lt;james.ford=pareidolia.rocks@groups.io&gt; wrote:<br><br></blockquote><blockquote><div dir="ltr">﻿<meta http-equiv="content-type">Been a lot of great ideas, patterns and suggestions….<div><br></div><div>In the end I think it’s always the same…. Find the seams, encapsulate the ugliness, isolate it behind an interface and evolve the service behind the interface….</div><div><br></div><div><br><br><div dir="ltr"><br><div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><span style="background-color: rgba(255, 255, 255, 0);">--&nbsp;<br></span><div class="m_7017788891221011597gmail_signature"><div dir="ltr"><i>James Ford</i><div><span style="background-color: rgba(255, 255, 255, 0);">Founder</span></div><div><span style="background-color: rgba(255, 255, 255, 0);">Pareidolia, LLC</span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><u>https://www.pareidolia.rocks</u></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br></span></div><div><span style="background-color: rgba(255, 255, 255, 0);"><br>"Where Vision meets Reality"</span></div></div></div></div></div><div dir="ltr"><br><blockquote>On Apr 28, 2022, at 2:54 PM, Erik Brandsberg &lt;erik@heimdalldata.com&gt; wrote:<br><br></blockquote></div><blockquote><div dir="ltr">﻿<div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well, as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" rel="nofollow noopener" target="_blank">josiah@sunshower.io</a>&gt; wrote:<br></div><blockquote class="gmail_quote">I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!


  

<p></p><p></p></blockquote></div>


  

</div></blockquote></div>


  

</div></blockquote></div>
          </div>
          <script>
            $('#quoted-204315170').on('show.bs.collapse', function () {
              $('#qlabel-204315170').text("Hide quoted text");
            })
            $('#quoted-204315170').on('hide.bs.collapse', function () {
              $('#qlabel-204315170').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204315170" aria-expanded="false" aria-controls="window-204315170"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204315170"><span id="likebutton204315170"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204315170, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204315170" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204315170">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1615858"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204315170"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204315170"><span id="likestats204315170"></span></div>
        </div>
      </div>
      
        <div id="window-204315170" class="collapse">
          <form class="form" id="form204315170" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204315170" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204315170">
            <input type="hidden" id="groupname204315170" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204315170" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204315170" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204315170" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204315170">
    <textarea id="editor204315170" name="editor204315170" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204315170"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204315170"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204315170" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204315170" value="html">
              

              <div id="bccme204315170" class="checkbox">
                <label for="bccme204315170">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204315170" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204315170"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204315170" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204315170" name="preview" onclick="editor.PreviewMarkdown(204315170,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204315170" name="return" onclick="editor.ReturnMarkdown(204315170)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204315170" data-toggle="collapse" data-target="#window-204315170"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204315170" onclick="editor.TogglePrivate('204315170', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204315170" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204315170">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204315170">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204315170" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204315170&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204315170" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204315170">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204315170">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204315170" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204315170&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204315170').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204315170').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204315170", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204315170').tooltip()
            $('#showHistory204315170').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204315170, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204315170, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5202"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    kkmiller
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 2:53pm">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5202"><span class="hidden-xs">#5202&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204316310">
        <div class="forcebreak" dir="auto"><div dir="ltr">Rust or Bust in God We Trust. Refactor Rebuild Rebase.<div>We can almost justify any expense we make.</div></div><br></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204316310" role="button" data-toggle="collapse" href="#quoted-204316310" aria-expanded="false" aria-controls="quoted-204316310"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204316310" class="collapse forcebreak">
            <div dir="auto"><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 3:19 PM james Ford &lt;james.ford@pareidolia.rocks&gt; wrote:<br></div><blockquote class="gmail_quote"><div>Been a lot of great ideas, patterns and suggestions….<div><br></div><div>In the end I think it’s always the same…. Find the seams, encapsulate the ugliness, isolate it behind an interface and evolve the service behind the interface….</div><div><br></div><div><br><br><div dir="ltr"><br><div><div><span style="background-color:rgba(255,255,255,0);"><br></span></div><div><span style="background-color:rgba(255,255,255,0);"><br></span></div><span style="background-color:rgba(255,255,255,0);">--&nbsp;<br></span><div><div dir="ltr"><i>James Ford</i><div><span style="background-color:rgba(255,255,255,0);">Founder</span></div><div><span style="background-color:rgba(255,255,255,0);">Pareidolia, LLC</span></div><div><span style="background-color:rgba(255,255,255,0);"><br></span></div><div><span style="background-color:rgba(255,255,255,0);"><u><a href="https://www.pareidolia.rocks" target="_blank" rel="nofollow noopener">https://www.pareidolia.rocks</a></u></span></div><div><span style="background-color:rgba(255,255,255,0);"><br></span></div><div><span style="background-color:rgba(255,255,255,0);"><br>"Where Vision meets Reality"</span></div></div></div></div></div><div dir="ltr"><br><blockquote>On Apr 28, 2022, at 2:54 PM, Erik Brandsberg &lt;<a href="mailto:erik@heimdalldata.com" target="_blank" rel="nofollow noopener">erik@heimdalldata.com</a>&gt; wrote:<br><br></blockquote></div><blockquote><div dir="ltr">﻿<div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well, as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" target="_blank" rel="nofollow noopener">josiah@sunshower.io</a>&gt; wrote:<br></div><blockquote class="gmail_quote">I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!


  

<p></p><p></p></blockquote></div>


  

</div></blockquote></div></div>


  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204316310').on('show.bs.collapse', function () {
              $('#qlabel-204316310').text("Hide quoted text");
            })
            $('#quoted-204316310').on('hide.bs.collapse', function () {
              $('#qlabel-204316310').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204316310" aria-expanded="false" aria-controls="window-204316310"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204316310"><span id="likebutton204316310"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204316310, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204316310" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204316310">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1388229"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204316310"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204316310"><span id="likestats204316310"></span></div>
        </div>
      </div>
      
        <div id="window-204316310" class="collapse">
          <form class="form" id="form204316310" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204316310" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204316310">
            <input type="hidden" id="groupname204316310" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204316310" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204316310" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204316310" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204316310">
    <textarea id="editor204316310" name="editor204316310" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204316310"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204316310"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204316310" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204316310" value="html">
              

              <div id="bccme204316310" class="checkbox">
                <label for="bccme204316310">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204316310" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204316310"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204316310" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204316310" name="preview" onclick="editor.PreviewMarkdown(204316310,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204316310" name="return" onclick="editor.ReturnMarkdown(204316310)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204316310" data-toggle="collapse" data-target="#window-204316310"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204316310" onclick="editor.TogglePrivate('204316310', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204316310" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204316310">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204316310">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204316310" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204316310&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204316310" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204316310">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204316310">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204316310" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204316310&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204316310').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204316310').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204316310", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204316310').tooltip()
            $('#showHistory204316310').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204316310, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204316310, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5203"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Kris Ciccarelli
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 3:08pm">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5203"><span class="hidden-xs">#5203&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204316996">
        <div class="forcebreak" dir="auto"><meta http-equiv="content-type">Currently in the middle of a from scratch rewrite started by previous leadership, which was already promised before I even started. &nbsp;Scary enough to tackle a greenfield rewrite, but when you don’t get to pick the team, timeline, plan, technology it’s even more fun…<div><br></div><div>My friend Dan wrote a great blogpost about this that I still read whenever I get involved in one of these projects. Definitely worth a read!&nbsp;</div><div><br></div><div><a href="https://www.onstartups.com/tabid/3339/bid/97052/How-To-Survive-a-Ground-Up-Rewrite-Without-Losing-Your-Sanity.aspx" rel="nofollow noopener" target="_blank">https://www.onstartups.com/tabid/3339/bid/97052/How-To-Survive-a-Ground-Up-Rewrite-Without-Losing-Your-Sanity.aspx</a><br><br><div dir="ltr">-Kris</div><div dir="ltr"><br></div></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204316996" role="button" data-toggle="collapse" href="#quoted-204316996" aria-expanded="false" aria-controls="quoted-204316996"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204316996" class="collapse forcebreak">
            <div dir="auto"><blockquote>On Apr 28, 2022, at 2:54 PM, Erik Brandsberg &lt;erik@heimdalldata.com&gt; wrote:<br><br></blockquote><blockquote><div dir="ltr">﻿<div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well, as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" rel="nofollow noopener" target="_blank">josiah@sunshower.io</a>&gt; wrote:<br></div><blockquote class="gmail_quote">I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!


  

<p></p><p></p></blockquote></div>


  

</div></blockquote></div>
          </div>
          <script>
            $('#quoted-204316996').on('show.bs.collapse', function () {
              $('#qlabel-204316996').text("Hide quoted text");
            })
            $('#quoted-204316996').on('hide.bs.collapse', function () {
              $('#qlabel-204316996').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204316996" aria-expanded="false" aria-controls="window-204316996"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204316996"><span id="likebutton204316996"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204316996, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204316996" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204316996">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:6208285"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204316996"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204316996"><span id="likestats204316996"></span></div>
        </div>
      </div>
      
        <div id="window-204316996" class="collapse">
          <form class="form" id="form204316996" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204316996" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204316996">
            <input type="hidden" id="groupname204316996" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204316996" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204316996" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204316996" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204316996">
    <textarea id="editor204316996" name="editor204316996" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204316996"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204316996"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204316996" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204316996" value="html">
              

              <div id="bccme204316996" class="checkbox">
                <label for="bccme204316996">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204316996" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204316996"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204316996" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204316996" name="preview" onclick="editor.PreviewMarkdown(204316996,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204316996" name="return" onclick="editor.ReturnMarkdown(204316996)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204316996" data-toggle="collapse" data-target="#window-204316996"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204316996" onclick="editor.TogglePrivate('204316996', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204316996" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204316996">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204316996">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204316996" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204316996&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204316996" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204316996">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204316996">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204316996" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204316996&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204316996').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204316996').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204316996", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204316996').tooltip()
            $('#showHistory204316996').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204316996, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204316996, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5204"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Michael Crabtree
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="Apr 28, 2022 3:29pm">Apr 28</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5204"><span class="hidden-xs">#5204&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204317812">
        <div class="forcebreak" dir="auto"><meta http-equiv="Content-Type">



<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
Erik,</div>
<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
<br>
</div>
<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
That is why I love Heimdalldata! you really helped out our enterprise healthcare client with the data proxy and I am convinced it will help most of my clients facing performance and security concerns with database connections.</div>
<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
<br>
</div>
<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
keep up the great work!</div>
<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
<br>
</div>
<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
<br>
</div>
<div>
<div style="font-family: Calibri, Arial, Helvetica, sans-serif;   font-size: 12pt;   color: rgb(0, 0, 0);">
<br>
</div>
<div id="Signature">
<div>
<div id="divtagdefaultwrapper" dir="ltr" style="font-size:12pt;   color:#000000;   font-family:Calibri,Arial,Helvetica,sans-serif;">
<p></p>
<p>Michael Crabtree | CEO - NETSYNTROPY</p>
<p><span>Outsmart Chaos</span>&nbsp;&nbsp;&nbsp; <a href="http://www.netsyntropy.com/?page_id=165" rel="nofollow noopener" target="_blank">
See our datasheet here: netsyntropy.com</a>&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>e. Michael.crabtree@netsyntropy.com | m. 949.562.3612 | o. 949.939.0689</p>
<br>
<p></p>
</div>
</div>
</div>
</div>
<div id="appendonsend"></div></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204317812" role="button" data-toggle="collapse" href="#quoted-204317812" aria-expanded="false" aria-controls="quoted-204317812"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204317812" class="collapse forcebreak">
            <div dir="auto"><hr>
<div id="divRplyFwdMsg" dir="ltr"><font face="Calibri, sans-serif" color="#000000"><b>From:</b> worldwide@ctolunches.groups.io &lt;worldwide@ctolunches.groups.io&gt; on behalf of Erik Brandsberg via groups.io &lt;erik=heimdalldata.com@groups.io&gt;<br>
<b>Sent:</b> Thursday, April 28, 2022 11:54 AM<br>
<b>To:</b> Josiah Haswell &lt;josiah@sunshower.io&gt;<br>
<b>Cc:</b> worldwide &lt;worldwide@ctolunches.groups.io&gt;<br>
<b>Subject:</b> Re: [ctolunches] re-builds</font>
<div>&nbsp;</div>
</div>
<div>
<div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the
 db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well,
 as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div>
<br>
<div class="x_gmail_quote">
<div dir="ltr" class="x_gmail_attr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" rel="nofollow noopener" target="_blank">josiah@sunshower.io</a>&gt; wrote:<br>
</div>
<blockquote class="x_gmail_quote">
I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive
 UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!
<p></p>
<p></p>
</blockquote>
</div>

</div>

</div>
          </div>
          <script>
            $('#quoted-204317812').on('show.bs.collapse', function () {
              $('#qlabel-204317812').text("Hide quoted text");
            })
            $('#quoted-204317812').on('hide.bs.collapse', function () {
              $('#qlabel-204317812').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204317812" aria-expanded="false" aria-controls="window-204317812"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204317812"><span id="likebutton204317812"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204317812, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204317812" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204317812">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:6473472"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204317812"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204317812"><span id="likestats204317812"></span></div>
        </div>
      </div>
      
        <div id="window-204317812" class="collapse">
          <form class="form" id="form204317812" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204317812" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204317812">
            <input type="hidden" id="groupname204317812" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204317812" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204317812" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204317812" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204317812">
    <textarea id="editor204317812" name="editor204317812" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204317812"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204317812"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204317812" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204317812" value="html">
              

              <div id="bccme204317812" class="checkbox">
                <label for="bccme204317812">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204317812" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204317812"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204317812" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204317812" name="preview" onclick="editor.PreviewMarkdown(204317812,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204317812" name="return" onclick="editor.ReturnMarkdown(204317812)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204317812" data-toggle="collapse" data-target="#window-204317812"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204317812" onclick="editor.TogglePrivate('204317812', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204317812" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204317812">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204317812">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204317812" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204317812&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204317812" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204317812">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204317812">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204317812" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204317812&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204317812').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204317812').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204317812", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204317812').tooltip()
            $('#showHistory204317812').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204317812, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204317812, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5208"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Jon Stockdill
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="May 1, 2022 5:09am">May 1</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5208"><span class="hidden-xs">#5208&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204422959">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div>Bring the discussion back to the business outcomes (KPI/OKRs), then the big-bang rebuild may not be the right decision.&nbsp; Often, the most costly&nbsp;drag is in one or two features.<br></div><div><br></div><div>More than likely, the most costly drag is also the most complicated business logic, that is also poorly defined (both requirements and offering).&nbsp; ie, junk in equals junk out.&nbsp; Re-building the application should also mean "re-building the offering".&nbsp; &nbsp;While&nbsp;rebuilding the offering, the cost of rebuilding can be reduced.</div><div><br></div><div>TL;DR:&nbsp; Messy code comes from messy business.&nbsp; &nbsp;Clean up the business too or make a more modern mess.</div><div><br></div><div><div dir="ltr" class="gmail_signature"><div dir="ltr"><div>--jon (he, him, his)</div><div><br></div></div></div></div></div><br></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204422959" role="button" data-toggle="collapse" href="#quoted-204422959" aria-expanded="false" aria-controls="quoted-204422959"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204422959" class="collapse forcebreak">
            <div dir="auto"><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 6:29 PM Michael Crabtree &lt;<a href="mailto:michael.crabtree@netsyntropy.com" rel="nofollow noopener" target="_blank">michael.crabtree@netsyntropy.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">




<div dir="ltr">
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
Erik,</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
That is why I love Heimdalldata! you really helped out our enterprise healthcare client with the data proxy and I am convinced it will help most of my clients facing performance and security concerns with database connections.</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
keep up the great work!</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div id="gmail-m_-7877299176562726150Signature">
<div>
<div id="gmail-m_-7877299176562726150divtagdefaultwrapper" dir="ltr" style="font-size:12pt;  color:rgb(0,0,0);  font-family:Calibri,Arial,Helvetica,sans-serif;">
<p></p>
<p>Michael Crabtree | CEO - NETSYNTROPY</p>
<p><span>Outsmart Chaos</span>&nbsp;&nbsp;&nbsp; <a href="http://www.netsyntropy.com/?page_id=165" target="_blank" rel="nofollow noopener">
See our datasheet here: netsyntropy.com</a>&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>e. <a href="mailto:Michael.crabtree@netsyntropy.com" target="_blank" rel="nofollow noopener">Michael.crabtree@netsyntropy.com</a> | m. 949.562.3612 | o. 949.939.0689</p>
<br>
<p></p>
</div>
</div>
</div>
</div>
<div id="gmail-m_-7877299176562726150appendonsend"></div>
<hr>
<div id="gmail-m_-7877299176562726150divRplyFwdMsg" dir="ltr"><font face="Calibri, sans-serif" color="#000000"><b>From:</b> <a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a> &lt;<a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a>&gt; on behalf of Erik Brandsberg via <a href="http://groups.io" target="_blank" rel="nofollow noopener">groups.io</a> &lt;erik=<a href="mailto:heimdalldata.com@groups.io" target="_blank" rel="nofollow noopener">heimdalldata.com@groups.io</a>&gt;<br>
<b>Sent:</b> Thursday, April 28, 2022 11:54 AM<br>
<b>To:</b> Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" target="_blank" rel="nofollow noopener">josiah@sunshower.io</a>&gt;<br>
<b>Cc:</b> worldwide &lt;<a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a>&gt;<br>
<b>Subject:</b> Re: [ctolunches] re-builds</font>
<div>&nbsp;</div>
</div>
<div>
<div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the
 db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well,
 as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div>
<br>
<div>
<div dir="ltr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" target="_blank" rel="nofollow noopener">josiah@sunshower.io</a>&gt; wrote:<br>
</div>
<blockquote>
I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive
 UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!
<p></p>
<p></p>
</blockquote>
</div>

</div>
</div>



  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204422959').on('show.bs.collapse', function () {
              $('#qlabel-204422959').text("Hide quoted text");
            })
            $('#quoted-204422959').on('hide.bs.collapse', function () {
              $('#qlabel-204422959').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204422959" aria-expanded="false" aria-controls="window-204422959"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204422959"><span id="likebutton204422959"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204422959, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204422959" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204422959">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1661920"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204422959"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204422959"><span id="likestats204422959"></span></div>
        </div>
      </div>
      
        <div id="window-204422959" class="collapse">
          <form class="form" id="form204422959" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204422959" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204422959">
            <input type="hidden" id="groupname204422959" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204422959" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204422959" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204422959" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204422959">
    <textarea id="editor204422959" name="editor204422959" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204422959"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204422959"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204422959" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204422959" value="html">
              

              <div id="bccme204422959" class="checkbox">
                <label for="bccme204422959">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204422959" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204422959"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204422959" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204422959" name="preview" onclick="editor.PreviewMarkdown(204422959,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204422959" name="return" onclick="editor.ReturnMarkdown(204422959)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204422959" data-toggle="collapse" data-target="#window-204422959"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204422959" onclick="editor.TogglePrivate('204422959', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204422959" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204422959">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204422959">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204422959" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204422959&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204422959" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204422959">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204422959">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204422959" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204422959&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204422959').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204422959').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204422959", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204422959').tooltip()
            $('#showHistory204422959').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204422959, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204422959, false)
      </script>
    
    
  </tr>



    
  
  
  <tr class="test">
    <td>
    
    <hr class="sr-only">
    <a name="5210"></a>
      


      <div class="row">
        <div class="col-md-12">
          <div class="pull-left">
            
            
              
                
  
    
      <i class="fa fa-user fa-3x"></i>
    
    
  
	
    Alan Blount
	

  

              
            
          </div>
          <div class="pull-right" style="text-align: right;">
            <font size="-1" class="text-muted">
              
<span title="May 1, 2022 7:42pm">May 1</span>

            </font>
            &nbsp; 
            <a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/message/5210"><span class="hidden-xs">#5210&nbsp;&nbsp;</span><i class="fa fa-link fa-lg"></i></a>
            
          </div>
        </div>
      </div>
      <br>
      <div id="msgbody204456224">
        <div class="forcebreak" dir="auto"><div dir="ltr"><div class="gmail_default" style="font-family:verdana,sans-serif;">I love that this is a super active thread, and no surprise, as we have all been faced with similar choices... and there are no foolproof methods of estimating the project or executing it.&nbsp; As others&nbsp;have pointed out, a lot of it comes to state management and if old and new can co-exist, and impact to users (ideally minimal or zero).</div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;">This is a 2004 book, but it's a great perspective on the problem, if you're a book reader: "Working Effectively with Legacy Code" (<a href="https://www.oreilly.com/library/view/working-effectively-with/0131177052/" rel="nofollow noopener" target="_blank">oreilly</a>&nbsp;<a href="https://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052" rel="nofollow noopener" target="_blank">amazon</a>).</div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;">If you were to ask me to do this, a lot depends on context I don't have, but 1st instinct tells me a strangler pattern is correct, and I'd probably propose something like this:</div><div class="gmail_default" style=""><ul style="font-family:verdana,sans-serif;"><li>Write a proxy in elixir/phoenix and make that the new front end - a straight passthrough http proxy in a (new) application server language/framework</li><li>Isolate segments / microservices / modules (potentially on the old codebase first, and then on the new)</li><li>Write new code in elixir/phoenix</li><li>Shadow traffic to both old and new, log into a shadow DB or logs and ensure identical functionality</li><li>Migrate segments / microservices / modules after proving they are functional</li><li>Keep the old code in shadow mode in case of problems, for a few months</li><li>Wash, rinse, and repeat</li></ul><div style=""><font face="verdana, sans-serif">If you felt like splitting off the front end and making the backend application stack API only, that should either come before or after this language migration....&nbsp; but it would certainly make this process easier, as you'd only be mirroring API and business logic, not also front end.&nbsp; Similarly, if you want to change DB, you may want to wait for another migration... or you could possibly keep the old and new DB in perfect sync, with lots of audits and alerts if not in sync (</font><font face="monospace">select&nbsp;primarykey, fingerprint(old.field)=fingerprint(new.field) from old left join new using primarykey</font><font face="verdana, sans-serif">)</font></div></div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;">If you do ... well, pretty much anything else ... you should probably think of this as a new application which may have a migration path from the old one... not a re-write, but a write.</div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;">If the client wants to keep their application, this is actually a <i>great</i> investment.&nbsp; Right now, it's probably a bit toxic to work on it, people are scared, bugs are introduced to prod and nobody knows until clients complain... It's probably a mess.&nbsp; Your job is to ensure the client understands that it is probably not sustainable in its current form... sooner or later they will have to deal with this problem, or freeze the app in its current state forever, or walk away.&nbsp; When the foundation of a house is untrustworthy, all the paint or remodeling work you want to do is a waste until you face up to fixing the foundation.</div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;">Good luck!&nbsp; You can do it, just be cautious, especially about state replication.</div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div class="gmail_default" style="font-family:verdana,sans-serif;"><br></div><div><div dir="ltr" class="gmail_signature"><div dir="ltr">Thanks,<div>-alan</div></div></div></div><br></div><br></div>
        
          <a class="label hashtag-label-sage" id="qlabel-204456224" role="button" data-toggle="collapse" href="#quoted-204456224" aria-expanded="false" aria-controls="quoted-204456224"><span class="sr-only">toggle quoted message</span>Show quoted text</a>
          <p>
          </p><div id="quoted-204456224" class="collapse forcebreak">
            <div dir="auto"><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Sun, May 1, 2022 at 6:09 AM Jon Stockdill &lt;<a href="mailto:jon.stockdill@gmail.com" rel="nofollow noopener" target="_blank">jon.stockdill@gmail.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote"><div dir="ltr"><div>Bring the discussion back to the business outcomes (KPI/OKRs), then the big-bang rebuild may not be the right decision.&nbsp; Often, the most costly&nbsp;drag is in one or two features.<br></div><div><br></div><div>More than likely, the most costly drag is also the most complicated business logic, that is also poorly defined (both requirements and offering).&nbsp; ie, junk in equals junk out.&nbsp; Re-building the application should also mean "re-building the offering".&nbsp; &nbsp;While&nbsp;rebuilding the offering, the cost of rebuilding can be reduced.</div><div><br></div><div>TL;DR:&nbsp; Messy code comes from messy business.&nbsp; &nbsp;Clean up the business too or make a more modern mess.</div><div><br></div><div><div dir="ltr"><div dir="ltr"><div>--jon (he, him, his)</div><div><br></div></div></div></div></div><br><div class="gmail_quote"><div dir="ltr" class="gmail_attr">On Thu, Apr 28, 2022 at 6:29 PM Michael Crabtree &lt;<a href="mailto:michael.crabtree@netsyntropy.com" target="_blank" rel="nofollow noopener">michael.crabtree@netsyntropy.com</a>&gt; wrote:<br></div><blockquote class="gmail_quote">




<div dir="ltr">
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
Erik,</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
That is why I love Heimdalldata! you really helped out our enterprise healthcare client with the data proxy and I am convinced it will help most of my clients facing performance and security concerns with database connections.</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
keep up the great work!</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div>
<div style="font-family:Calibri,Arial,Helvetica,sans-serif;  font-size:12pt;  color:rgb(0,0,0);">
<br>
</div>
<div id="gmail-m_-8281256951850610622gmail-m_-7877299176562726150Signature">
<div>
<div id="gmail-m_-8281256951850610622gmail-m_-7877299176562726150divtagdefaultwrapper" dir="ltr" style="font-size:12pt;  color:rgb(0,0,0);  font-family:Calibri,Arial,Helvetica,sans-serif;">
<p></p>
<p>Michael Crabtree | CEO - NETSYNTROPY</p>
<p><span>Outsmart Chaos</span>&nbsp;&nbsp;&nbsp; <a href="http://www.netsyntropy.com/?page_id=165" target="_blank" rel="nofollow noopener">
See our datasheet here: netsyntropy.com</a>&nbsp;&nbsp;&nbsp;&nbsp;</p>
<p>e. <a href="mailto:Michael.crabtree@netsyntropy.com" target="_blank" rel="nofollow noopener">Michael.crabtree@netsyntropy.com</a> | m. 949.562.3612 | o. 949.939.0689</p>
<br>
<p></p>
</div>
</div>
</div>
</div>
<div id="gmail-m_-8281256951850610622gmail-m_-7877299176562726150appendonsend"></div>
<hr>
<div id="gmail-m_-8281256951850610622gmail-m_-7877299176562726150divRplyFwdMsg" dir="ltr"><font face="Calibri, sans-serif" color="#000000"><b>From:</b> <a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a> &lt;<a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a>&gt; on behalf of Erik Brandsberg via <a href="http://groups.io" target="_blank" rel="nofollow noopener">groups.io</a> &lt;erik=<a href="mailto:heimdalldata.com@groups.io" target="_blank" rel="nofollow noopener">heimdalldata.com@groups.io</a>&gt;<br>
<b>Sent:</b> Thursday, April 28, 2022 11:54 AM<br>
<b>To:</b> Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" target="_blank" rel="nofollow noopener">josiah@sunshower.io</a>&gt;<br>
<b>Cc:</b> worldwide &lt;<a href="mailto:worldwide@ctolunches.groups.io" target="_blank" rel="nofollow noopener">worldwide@ctolunches.groups.io</a>&gt;<br>
<b>Subject:</b> Re: [ctolunches] re-builds</font>
<div>&nbsp;</div>
</div>
<div>
<div dir="ltr">I'm going to add my $.02 in.&nbsp; I like Java myself, and use it for our product, which looks at the modernization issue from a different approach.&nbsp; We provide a database proxy that provides a variety of services between often legacy apps and the
 db, including caching, connection management (with multiplexing), visibility, etc.&nbsp; Often, customers can use us to reduce the load on the DB and improve response time to older apps without having to rebuild them.&nbsp; The visibility aspects are useful as well,
 as it presents wait time differently than many other tools and helps you spot the areas really impacting performance.&nbsp; Rewrites aren't always the answer...</div>
<br>
<div>
<div dir="ltr">On Thu, Apr 28, 2022 at 2:01 PM Josiah Haswell &lt;<a href="mailto:josiah@sunshower.io" target="_blank" rel="nofollow noopener">josiah@sunshower.io</a>&gt; wrote:<br>
</div>
<blockquote>
I'd like to second Dominic's point here as I don't think I was clear before.&nbsp; "Boring" tech is awesome, and most surprises in software are unpleasant ones. I love Java+Spring+Vaadin (which you might consider--I've never,&nbsp;<em>ever</em> worked in a more productive
 UI environment than Vaadin), and the only surprise I've basically ever encountered is how rich and robust they are.&nbsp; That said, I think PHP/Laravel are a rock-solid choice for the same reasons!
<p></p>
<p></p>
</blockquote>
</div>

</div>
</div>



  

<p></p><p></p></blockquote></div>


  

<p></p><p></p></blockquote></div></div>
          </div>
          <script>
            $('#quoted-204456224').on('show.bs.collapse', function () {
              $('#qlabel-204456224').text("Hide quoted text");
            })
            $('#quoted-204456224').on('hide.bs.collapse', function () {
              $('#qlabel-204456224').text("Show quoted text");
            })
          </script>
        
        
        
      </div>

      
      <p>

      </p></td>
    </tr>

  
    <tr class="test">
      <td>
      <div class="row">
        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            
              <a data-toggle="collapse" href="#window-204456224" aria-expanded="false" aria-controls="window-204456224"><i class="fa fa-reply"></i> Reply</a>
            
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <center><span id="likebutton204456224"><span id="likebutton204456224"><a href="#" onclick="doLike(&quot;/g/worldwide&quot;,0,204456224, true, &quot;5276883099450123193&quot;);return false;"><i class="fa fa-thumbs-up"></i> Like</a></span></span></center>
          </div>
        

        
          <div class="col-xs-4 col-sm-2 col-md-2 col-lg-2">
            <div class="btn-group dropup pull-right">
              <a id="moredrop-204456224" href="#" data-target="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><i class="fa fa-bars"></i> More</a>
              <ul class="dropdown-menu" aria-labelledby="moredrop-204456224">

                

                

                  
                    
                  

                  


                  

                  

                  
                    <li><a rel="nofollow" href="https://ctolunches.groups.io/g/worldwide/search?q=posterid:1406010"><i class="fa-fw fa fa-comments"></i> All Messages By This Member</a></li>
                  

                  
                    <li><a href="#" data-toggle="modal" data-target="#reportMessageModal" data-message-id="204456224"><i class="fa-fw fa fa-flag"></i> Report This Message</a></li>
                  
                
              </ul>
            </div>
          </div>
        </div>        
      
      <div class="row">
        <div class="col-xs-12">
          <div id="likestats204456224"><span id="likestats204456224"></span></div>
        </div>
      </div>
      
        <div id="window-204456224" class="collapse">
          <form class="form" id="form204456224" method="POST" action="https://ctolunches.groups.io/g/worldwide/reply?p=Created,,,20,1,20,0" accept-charset="UTF-8">
            
              <input type="hidden" id="csrf204456224" name="csrf" value="5276883099450123193">
            
            <input type="hidden" name="mid" value="204456224">
            <input type="hidden" id="groupname204456224" name="groupname" value="/g/worldwide">
            <input type="hidden" id="draftid204456224" name="draftid" value="">
            <input type="hidden" name="single" value="">
            <input type="hidden" id="origsubject204456224" value="Private: Re: re-builds">
            <p><br>
            
              From: Nikhil Singh &lt;nikhil@tektorch.com.au&gt;
            
            </p><div class="form-group">
              <input name="subject" class="form-control" id="subject204456224" type="text" placeholder="Subject" value="Private: Re: re-builds" spellcheck="true">
            </div>
            
<div class="form-group">



  <div id="editwindow204456224">
    <textarea id="editor204456224" name="editor204456224" class="form-control input-sm" rows="10" style="visibility:hidden"></textarea>
  </div>

  <div id="previewWindow204456224"></div>
  

  

</div>

  <div class="form-group"></div>

  <div id="attachments204456224"></div>

<script>
function setContent(teditor) {
  teditor.setContent("");
}
</script>

            <input type="hidden" name="isprivate" id="isprivate204456224" value="">
            <div class="form-group">
              
                <input type="hidden" name="bodytype" id="bodytype204456224" value="html">
              

              <div id="bccme204456224" class="checkbox">
                <label for="bccme204456224">
                  <input type="checkbox" name="bccme" value="1">
                  BCC Me
                </label>
              </div>

              

              <div class="row">
                <div class="col-xs-12 btn-toolbar">
                
                  <input type="hidden" name="reply" id="replytype204456224" value="sender">
                  <button class="btn btn-primary btn-sm bottom10" id="replybutton204456224"><i class="fa fa-user"></i> Reply to Author</button>
                

                <span id="markdownbuttons204456224" style="display:none;">
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="preview204456224" name="preview" onclick="editor.PreviewMarkdown(204456224,&quot;/g/worldwide&quot;)"><i class="fa fa-search"></i> Preview</a>
                  <a href="javascript:void(0)" class="btn btn-default btn-sm bottom10" id="return204456224" name="return" onclick="editor.ReturnMarkdown(204456224)"><i class="fa fa-search"></i> Edit</a>
                </span>

                <button type="button" class="pull-right btn btn-danger btn-sm bottom10" name="cancel" value="Cancel" id="cancel-204456224" data-toggle="collapse" data-target="#window-204456224"><i class="fa fa-trash-alt"></i> Discard</button>

                
                  
                    <button class="pull-right btn btn-default btn-sm bottom10" type="button" id="private204456224" onclick="editor.TogglePrivate('204456224', 1, 0);return false;">Group Reply</button>
                    
                  
                

                </div>
              </div>
            </div>

            
<!-- Add Attachments Modal -->
<div class="modal fade" id="addAttachmentsModal204456224" tabindex="-1" role="dialog" aria-labelledby="addAttachmentsModalLabel204456224">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addAttachmentsModalLabel204456224">Upload Attachments</h4>
      </div>
      <div class="modal-body">
        <input id="attachmentupload204456224" name="fileupload" type="file" multiple="true">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#attachmentupload204456224&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>

<!-- Add Pictures Modal -->
<div class="modal fade" id="addPicturesModal204456224" tabindex="-1" role="dialog" aria-labelledby="addPicturesModalLabel204456224">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Done</span></button>
        <h4 class="modal-title" id="addPicturesModalLabel204456224">Insert Images</h4>
      </div>
      <div class="modal-body">
        <input id="pictureupload204456224" name="fileupload" type="file" multiple="true">
        <!--
        <p><br>
        <div class="form-group">
          <label for="url">Image URL</label>
          <input name="url" id="url" class="form-control input-sm" type="text">
        </div>
        -->
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-sm btn-default" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
        <button type="button" class="btn btn-sm btn-primary" onclick="$(&quot;#pictureupload204456224&quot;).fileinput(&quot;upload&quot;);"><i class="fa fa-file"></i> Add</button>
      </div>
    </div>
  </div>
</div>


          </form>
        </div>
        
        <script>
          $('#form204456224').submit(function(e){
            editor.ClearTimeout();
            /*
            if (postVar != null) {
              postVar.abort();
            }
            */
            deleted = true;
            if( $(this).hasClass('form-submitted') ){
              e.preventDefault();
              return;
            }
            $(this).addClass('form-submitted');
          });

          $('#window-204456224').on('show.bs.collapse', function (event) {
            // on opening of reply window
            editor.InitReplyDraft("204456224", "html", "0", "/g/worldwide", "5276883099450123193", 0, false, "");
          })
          if (document.documentElement.clientWidth > 767) {
            $('#addAttachmentsButton204456224').tooltip()
            $('#showHistory204456224').tooltip()
          }
        </script>
        
      
    </td>
    
      <script>
        displayLikes("/g/worldwide", 0, 204456224, false, "5276883099450123193")
      </script>
    
    
      <script>
        displayLikeStats("/g/worldwide", 0, 204456224, false)
      </script>
    
    
  </tr>



</tbody></table>

<form class="form" method="POST" action="https://ctolunches.groups.io/g/worldwide/editmessage">
  
    <input type="hidden" name="csrf" value="5276883099450123193">
  
  <input type="hidden" name="mid" id="mid" value="0">
  <input type="hidden" name="action_type" id="action_type" value="delete">

  <!-- Verify Remove Modal -->
  <div class="modal fade" id="deleteMessageModal" tabindex="-1" role="dialog" aria-labelledby="deleteMessageModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
          <h4 class="modal-title" id="deleteMessageModalLabel">Verify Delete</h4>
        </div>
        <div class="modal-body">
        Are you sure you wish to delete this message from the message archives of worldwide@ctolunches.groups.io? <strong>This cannot be undone.</strong>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
          <button class="btn btn-danger btn-sm" name="delmessage" value="1"><i class="fa fa-trash-alt"></i> Yes</button>
        </div>
      </div>
    </div>
  </div>
</form>

  <form class="form" method="POST" action="https://ctolunches.groups.io/g/worldwide/repostmessage">
    
      <input type="hidden" name="csrf" value="5276883099450123193">
    
    <input type="hidden" name="mid" id="repostmid" value="0">
    <input type="hidden" name="r" value="https://ctolunches.groups.io/g/worldwide/messages">

    <!-- Verify Repost Modal -->
    <div class="modal fade" id="repostMessageModal" tabindex="-1" role="dialog" aria-labelledby="repostMessageModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title" id="repostMessageModalLabel">Verify Repost</h4>
          </div>
          <div class="modal-body">
          Are you sure you wish to repost this message?
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
            <button class="btn btn-danger btn-sm" name="delmessage" value="1"><i class="fa fa-retweet"></i> Yes</button>
          </div>
        </div>
      </div>
    </div>
  </form>


  <form class="form" id="reportform" method="POST" action="https://ctolunches.groups.io/g/worldwide/report">
    
      <input type="hidden" name="csrf" value="5276883099450123193">
    
    <input type="hidden" name="mid" id="reportmid" value="0">

    <!-- Report Message Modal -->
    <div class="modal fade" id="reportMessageModal" tabindex="-1" role="dialog" aria-labelledby="reportMessageModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
            <h4 class="modal-title" id="reportMessageModalLabel">Report Message</h4>
          </div>
          <div class="modal-body">
            <label for="reason">Reason</label>
            <textarea id="reason" name="reason" class="form-control" rows="5"></textarea>

            <div class="radio">
              <label>
                <input type="radio" name="reportto" value="mods" checked="">Report to Moderators
              </label>
              <span class="help-block">I think this message isn't appropriate for our group. The Group moderators are responsible for maintaining their community and can address these issues.</span>
              <label>
                <input type="radio" name="reportto" value="support">Report to Groups.io Support
              </label>
              <span class="help-block">I think this violates the Terms of Service. This includes: harm to minors, violence or threats, harassment or privacy invasion, impersonation or misrepresentation, fraud or phishing.</span>
            </div>

            <p></p><center><strong>Note:</strong> Your email address is included with the abuse report.</center><p></p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
            <button type="submit" class="btn btn-danger btn-sm" name="report" value="1"><i class="fa fa-flag"></i> Report</button>
          </div>
        </div>
      </div>
    </div>
  </form>

  <script>
  $('#reportMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#reportmid').val(msgId);
  });
  $(function() {
    $('#reportform').on('submit', function(event){
        event.preventDefault(); 
        $('#reportMessageModal').modal('hide');
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),
            success: function(html) {
              createAlert("Your report has been sent", true);
            }
        });
        return false; 
    });
  });
  </script>


<form class="form" method="POST" action="https://ctolunches.groups.io/g/worldwide/editmessage">
  
    <input type="hidden" name="csrf" value="5276883099450123193">
  
  <input type="hidden" name="mid" id="splitmid" value="0">
  <input type="hidden" name="action_type" id="action_type" value="split">
  <input type="hidden" name="r" value="https://ctolunches.groups.io/g/worldwide/topic/90710568">
  <!-- Verify Split Modal -->
  <div class="modal fade" id="splitMessageModal" tabindex="-1" role="dialog" aria-labelledby="splitMessageModalLabel">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal"><span aria-hidden="true">×</span><span class="sr-only">Close</span></button>
          <h4 class="modal-title" id="splitMessageModalLabel">Split Topic</h4>
        </div>
        <div class="modal-body">
        <p>The new topic will begin with this message. Subject of the new topic:</p>
                <input name="subject" class="form-control" size="20" type="text" spellcheck="true">
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default btn-sm" data-dismiss="modal"><i class="fa fa-times"></i> Cancel</button>
          <button class="btn btn-danger btn-sm" name="delmessage" value="1"><i class="fa fa-trash-alt"></i> Split Topic</button>
        </div>
      </div>
    </div>
  </div>
</form>

<div class="row">
  <div class="col-xs-12">


  
    <div class="pull-right">
      <table>
        <tbody><tr>
          <td>
						
							21 - 34 of 34
						
          </td>
          <td>
            &nbsp;
          </td>
          <td>
            <ul class="pagination">
              
                <li><a href="https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p=Created%2C%2C%2C20%2C1%2C0%2C0&amp;prev=1"><i class="fa fa-chevron-left"><span class="sr-only">previous page</span></i></a></li>
              
              
                
                  <li><a href="https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p=Created%2C%2C%2C20%2C1%2C0%2C0&amp;jump=1" rel="nofollow">1</a></li>
                
              
                
                  <li class="disabled"><a class="currentpage" href="#">2</a></li>
                
              
              
                <li class="disabled"><a href="#"><i class="fa fa-chevron-right"><span class="sr-only">next page</span></i></a></li>
              
            </ul>
          </td>
        </tr>
      </tbody></table>
    </div>
  


<a href="https://ctolunches.groups.io/g/worldwide/topic/90797773?p=,,,20,0,0,0::,,,0,0,0,90797773" class="btn btn-default btn-sm"><i class="fa fa-arrow-left"></i><span class="hidden-xs">  Previous Topic</span></a>
<a href="https://ctolunches.groups.io/g/worldwide/topic/90839830?p=,,,20,0,0,0::,,,0,0,0,90839830" class="btn btn-default btn-sm"><i class="fa fa-arrow-right"></i><span class="hidden-xs"> Next Topic</span></a>

  </div>
</div>

<script>
  $('#deleteMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#mid').val(msgId);
  });
  $('#splitMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#splitmid').val(msgId);
  });
  $('#repostMessageModal').on('show.bs.modal', function(e) {
      var msgId = $(e.relatedTarget).data('message-id');
      $('#repostmid').val(msgId);
  });
  $('[id^=cancel]').on('click', function() {
      msg_num = $(this).attr('id').split("-")[1]
      $("#window-"+msg_num).collapse('hide')
  });

  if (location.hash) {
    location.href = location.hash;
  }

  $(".modal").on('shown.bs.modal', function () {
      $(this).find("input:visible:first").focus();
  });
  console.log("JSVERSION:", jsBundleVersion());
$("[data-toggle='tooltip']").tooltip();
</script>

<script>

  var nextPage = ""
  var ele = "#records div.test";
  var runawayCounter = 0;
  gioDestroy(function(event) {
    console.log("in gio:destroy for infinitescroll");
    console.log("destroying waypoints");
    $(ele).waypoint('destroy');
  });
  function initInfiniteScroll() {
    console.log("in initInfiniteScroll");
    if (nextPage == "") {
      console.log("At end");
      return;
    }
    console.log("numchildren: " + $(ele).children().length);
    var inView = isElementInView($(ele).last(), false);
    if (inView) {
      console.log('in view');
      if (nextPage == "") {
        console.log('at end');
        return;
      }
      runawayCounter++;
      if (runawayCounter > 5) {
        // failsafe to prevent infinite loop of fetching for whatever reason
        console.log("RUNAWAY")
        return
      }
      console.log('loading more');
      loadMore();
      return;
    }
    console.log("setting waypoint");
    thewaypoint = $(ele).last().waypoint(function(direction){
      console.log("in waypoint");
      $(this).waypoint('destroy');
      if(direction === "down") {
        console.log("Loading more")
        loadMore(); 
      }
    }, { offset: '100%'})
  }
  function loadMore(){
    if (nextPage == "") {
      return;
    }
    (function() {
      let urlstr = fixupURL("https://ctolunches.groups.io/g/worldwide/topic/re_builds/90710568?p="+nextPage+"&infinite=1");
      console.log("Fetching:", urlstr);
      num = 0;
      $.ajax({
        url: urlstr,
        cache: false,
        xhrFields: {
            withCredentials: true
        }
      }).done(function( data ) {
        $.each(data.Items, function(i,item) {
          $('#records').append($(item)[0]);
          num++;
        });
        
        console.log("Loaded " + num + " more")
        nextPage = data.NextPage;
        initInfiniteScroll();
      });
    })();
  }

  function isElementInView(element, fullyInView) {
    var pageTop = $(window).scrollTop();
    var pageBottom = pageTop + $(window).height();
    //var elementTop = $(element).offset().top;
    var elementTop = $(element).position().top;
    var elementBottom = elementTop + $(element).height();
  console.log("eletop:" + elementTop);
    if (fullyInView === true) {
        return ((pageTop < elementTop) && (pageBottom > elementBottom));
    } else {
        return ((elementTop <= pageBottom) && (elementBottom >= pageTop));
    }
  }

  if ($("#records").is("table") == true) {
    console.log("is a table");
    ele = "#records tr.test";
  }
  // activate dotdotdot because of dynamically loaded code
  
  if (document.documentElement.clientWidth <= 767) {
    nextPage = "";
    if (nextPage != "") {
      nextPage += "&next=1";
    }
    initInfiniteScroll();
  }

</script>




  
</div>
"""