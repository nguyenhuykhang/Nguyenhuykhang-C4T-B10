var s = document.getElementById("song_container");
console.log(s);




var deletebuttons = document.getElementsByClassName("btn_del");

for ( var i = 0; i < deletebuttons.length; i++) {
    var deletebutton = deletebuttons [i];
    deletebutton.addEventListener('click', function(e) {
        var del = e.target;
        var div = del.parentNode;
        div.remove();
    });
}

var editbuttons = document.getElementsByClassName('btn_e');

for (var a = 0; a < editbuttons.length; a++) {
    var editbutton = editbuttons [a];
    editbutton.addEventListener('click', function(f) {
        var edit = f.target;
        console.log(f.path[1].attributes[1].value);
    });
}
var btnadd = document.getElementsByClassName("btn_add");
for (var t = 0; t< btnn.length; t++) {
    btnadd[i].addEventListener("click",function(b) {
        var Songcontainer = document.getElementsById("song_container");
        var newHTML = <div class ="song" song_id = "78ab12">
       
        <h4 class="title">Girls like you</h4>
        <h5 class="artist">Maroon 5</h5>
        <button class="btn_del">Delete</button>
        <button class="btn_e">Edit</button>
        <button class="btn_more">More</button>
        <button class="btn_add">Add</button>


    </div>
        Songcontainer.insertAdjacentHTML("beforeend", newHTML)
    })
}