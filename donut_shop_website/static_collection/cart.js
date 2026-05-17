function delFromCart(e) {
  e.closest('div').remove();
}

function addToCart() {
  var cart = document.getElementById("donut_cart");
  var totalItems = document.getElementById("id_orderedDonuts-TOTAL_FORMS"); //hidden id for django formsets
  var itemCount = parseInt(totalItems.value);

  //clone last cart item
  var items = document.getElementsByClassName("cartItems");
  var lastItem = items[items.length-1];

  var newItem = lastItem.cloneNode(true);

  newItem.innerHTML = newItem.innerHTML.replace(new RegExp(`orderedDonuts-${itemCount-1}`,'g'), `orderedDonuts-${itemCount}`);
  newItem.style.display = "block";

  //add form (full-stack)
  totalItems.value = itemCount + 1;
  cart.appendChild(newItem);
  
}