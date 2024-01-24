const searchInput = document.getElementById('search-input');
const searchSuggestion = document.getElementById('search-suggestion');


function getHTTPObject(globalWindow){
    var xhr;
    if (globalWindow.XMLHttpRequest) {   
        xhr = new XMLHttpRequest();  
    } else if (globalWindow.ActiveXObject) {  
        try{
            xhr = new ActiveXObject("Msxml2.XMLHTTP");
        } catch(e) {     
            try {        
                xhr = new ActiveXObject("Microsoft.XMLHTTP");
            }catch(e) {        
                xhr = false;      
            }    
        }  
    }  
    return xhr;
}


function checkSearch(){
    let request = getHTTPObject(window);
    request.onreadystatechange = showSuggestions(request);
    request.open('GET', '/lyrics/json-api/', true);
    request.send(null);
}

let showSuggestions = (request) =>{
    return request.onreadystatechange = () =>{
        if(request.readyState == 4 && request.status == 200){
            data = JSON.parse(request.responseText)
            output = checkJsonFile(data);
            outputHtml(output);
        }
    }
}

function checkJsonFile(data){
    let matches = data.lyrics.filter(item => {
        const regex = new RegExp(`^${searchInput.value}`, 'gi'); 
        return item.title.match(regex) || item.song_writer.match(regex);

    });

    if(searchInput.value.length === 0){
        matches = [];
    }
    return matches;
}


function outputHtml(output){

    if(output.length > 0){
        result = output.map(match => 
            `<div class="card card-body mb-1">
                <div><a href="/lyrics/single/${match.slug}">${match.title}</a></div>
                <div><a href="/lyrics/single/${match.slug}" class="text-light">${match.song_writer}</a></div>
            </div>`
        ).join('');

        console.log('output');
        console.log(result);
        searchSuggestion.innerHTML = result;
    } 
}

searchInput.addEventListener('keyup', function(){
    checkSearch();
});
    



