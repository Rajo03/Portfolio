const myButton = document.getElementById("mybutton");
const myAnimation = document.getElementById("mydiv");

myButton.addEventListener("click", begin)

function begin(){
    let timerId = null;
    let scaleX = 1;
    let scaleY = 1;



    timerId = setInterval(frame, 5);

    function frame() {
        if(scaleX <= 0.1 || scaleY <= 0.1){
            clearInterval(timerId);

        }
        else{
            scaleX-=0.01;
            scaleY-=0.01;
            myAnimation.style.transform = "scale("+scaleX+","+scaleY+")";
            
    
        }

    }
}