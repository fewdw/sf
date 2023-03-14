$(document).ready(function() {
    $('#edit-btn').on('click', function() {
      // Enable editing of all fields
      $('#name').prop('readonly', false);
      $('#weight').prop('readonly', false);
      $('#weight-unit').prop('disabled', false);
      $('#height').prop('readonly', false);
      $('#age').prop('readonly', false);
      $('#fights').prop('readonly', false);
      $('#postal-code').prop('readonly', false);
      $('#language').prop('disabled', false);
      $('#experience').prop('readonly', false);
      $('#picture').prop('disabled', false);
      
      // Show save button and hide edit button
      $('#save-btn').removeClass('d-none');
      $('#edit-btn').addClass('d-none');
    });
    
    $('#save-btn').on('click', function() {
      // Disable editing of all fields
      $('#name').prop('readonly', true);
      $('#weight').prop('readonly', true);
      $('#weight-unit').prop('disabled', true);
      $('#height').prop('readonly', true);
      $('#age').prop('readonly', true);
      $('#fights').prop('readonly', true);
      $('#postal-code').prop('readonly', true);
      $('#language').prop('disabled', true);
      $('#experience').prop('readonly', true);
      $('#picture').prop('disabled', true);
      
      // Show edit button and hide save button
      $('#save-btn').addClass('d-none');
      $('#edit-btn').removeClass('d-none');
      
      // Show success message
      Swal.fire({
        icon: 'success',
        title: 'Information Saved',
        showConfirmButton: false,
        timer: 1500
      });
    });
  });