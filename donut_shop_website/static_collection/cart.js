function delFromCart(e) {
  e.closest('div').remove();
}

function addToCart() {
  var new_donuts = document.createElement("div")
  new_donuts.className = "cartItems";

  var donut_type = document.getElementById("type").value;
  var donut_flavour = document.getElementById("flavour").value;
  var donut_qty = document.getElementById("quantity").value;

  new_donuts.innerHTML = "<strong>"+donut_flavour+"</strong> - "+donut_type+" ("+donut_qty+"x)";
  new_donuts.innerHTML += "<button class='delItemBtn' onclick='delFromCart(this)'> X </button>";

  document.getElementById("donut_cart").appendChild(new_donuts);
}