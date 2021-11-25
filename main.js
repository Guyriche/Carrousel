function disapear(){
  var items = document.getElementsByClassName("hidden");
  for (i = 0; i < items.length; i++) {
            items[i].classList.add('show');
        }
}
