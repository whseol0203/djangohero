

function Login(){
    var idText = document.querySelector('#loginId').value;
    var passwordText = document.querySelector('#loginPwd').value;
    

    $.ajax({
        url: 'http://127.0.0.1:8000/login/',
        type: 'post',
        data: {
                "userId": `${idText}`,
                "password": `${passwordText}`
        },
        success: function (data){
            console.log(data)
            alert("데이터전송 성공");
        },
        error: function (error){
            console.log(data)
            alert("에러");
        }
    })

}




document.querySelector("#submitBtn").onclick = Login;
