let rules = "";

$('#dropdown').on('change', function() {
  var dropdownValue = $(this).val();
  gymSelection = dropdownValue;
  
  $.get('http://127.0.0.1:8080/api/gym/rules/' + gymSelection, function(data) {
    rules = data;
  });
});

$(document).ready(function() {
  $('#usegymrules').change(function() {
    if ($(this).is(':checked')) {
      var currentValue = $('#rules').val();
      if (currentValue === '') {
        $('#rules').val(rules);
      } else {
        $('#rules').val(currentValue + '\n' + rules);
      }
    } else {
      var currentValue = $('#rules').val();
      var newValue = currentValue.replace(new RegExp(rules.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&') + '\\n?', 'g'), '');
      $('#rules').val(newValue);
    }
  });
});
