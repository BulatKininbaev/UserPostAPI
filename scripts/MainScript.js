


function display(menu){

document.getElementById('table_list').style.visibility = (menu === 'list')?'visible':'hidden';
document.getElementById('input_info').style.visibility = (menu === 'add')?'visible':'hidden';


switch (menu) {
    case "list":
    //    GetList();
             }
}



function GetList(){
    let element = document.getElementById("table_list");

    const apiUrl = ' http://127.0.0.1:8000/users';

fetch(apiUrl)
.then(function (response) {
	// The API call was successful!
	return response.text();
}).then(function (html) {
	// This is the HTML from our response as a text string
	element.innerHTML =  html;
}).catch(function (err) {
	// There was an error
	console.warn('Something went wrong.', err);
});

}

function AddList(){

    const apiUrl = ' http://127.0.0.1:8000/users';

    let fio = document.getElementById('name').value;
    let user_name = document.getElementById('user_name').value;
    let user_address = document.getElementById('user_address').value;

    let  contactinfo = [{"name":fio,"user_name":user_name,"user_address":user_address}];
fetch(apiUrl, {
  method: "POST",
  body: JSON.stringify(contactinfo),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
  })
  .then((response) => response.json())
  .then((json) => console.log(json));


}
