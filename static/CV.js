//print my name to the console
console.log("Welcome to my Online CV page");
console.log("My name is Vered-Bar Arbel");

//change #imgID's src to newSrc. both should by string type
/*function changeImgSrc(imgID, newSrc){
    document.getElementById(imgID).src = newSrc;
}*/


//cv1: profile pic - view my photos by click
var photos = ["Images/photo1.jpeg", "Images/photo3.jpeg", "Images/photo2.jpeg"];
var i = 0;

function changeImgSrc(){
    if (i < photos.length){
        document.getElementById("profilePic").src = photos[i];
        window.setTimeout(changeImgSrc, 1700);
        i++;
    }
    else{
        i = 0;
    }

}


//cv2: show approval notification, IN CASE all fields are valid
function beInTouch(){
    if(phoneNum.checkValidity() & email.checkValidity()){
        alert("Thanks! \n We'll be in touch :)")
    }
}