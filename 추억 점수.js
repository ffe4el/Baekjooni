function solution(name, yearning, photo) {
    var answer = [];

    for(var i=0; i<photo.length; i++){
        var cnt = 0;
        for(var j=0; j<photo[i].length; j++){ //photo[0]하면 안됨...
            for(var k=0; k<name.length; k++){
                if(photo[i][j] === name[k]){
                    cnt += yearning[k];
                }
            }
        }
        //push를 한다...
        answer.push(cnt);
    }
    return answer;
}