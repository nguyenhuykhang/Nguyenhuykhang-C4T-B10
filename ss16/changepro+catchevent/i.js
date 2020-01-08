function starClick() {  // callback
    console.log("star click");
}

var btn = document.getElementById('btn');
btn.textContent = "Stop";
btn.addEventListener('click', function (e) {
    console.log(e);
});

var searchbar = document.getElementById("search_bar");
searchbar.value = "";
searchbar.style.backgroundColor = "blue";
searchbar.style.color = "#ffffff";

var menu = document.getElementById("menu");
menu.textContent = "";


// var lilist = menu.getElementsByTagName("Li");
// var firstli = lilist[0];
// firstli.remove();
var deletebuttons = document.getElementsByClassName("btn_delete");
for (var i = 0; i <deletebuttons.length; i++) {


    var deletebutton = deletebuttons[i];
    deletebutton.addEventListener('click', function(e) {
        var btn = e.target;
        var div = btn.parentNode;
        div.remove();
    })
}