function solution(players, callings) {
    var answer = [];
    for(var i=0; i<callings.length(); i++){
        for(var j=0; j<players.length(); j++){
            if(callings[i]==players[j]){
                callings[i]=players[j];
                players[j]=players[j-1];
            }
        }
    }
    for(var i=0; i<players.length(); i++){
        answer[i] = players[i];
    }

    return answer;
}


