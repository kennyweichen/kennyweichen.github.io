document.addEventListener('mousedown', function () {
    document.documentElement.classList.add('clicking');
  });
  
  document.addEventListener('mouseup', function () {
    document.documentElement.classList.remove('clicking');
  });

  document.addEventListener('mousedown', function () {
    document.body.classList.add('clicking');
  });
  
  document.addEventListener('mouseup', function () {
    document.body.classList.remove('clicking');
  });
  