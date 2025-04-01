

let SERVER_URL = 'http://127.0.0.1:5000/';
let sort_decending = false; // if truw will sort in ascending order
//let data = "{{ data }}";
//let data = '{{dbdata}}'//[{name: "Wings", cost :30 , time : 70} ] ;
let  cost_dict = {"High" : 2, "Medium":1, "Low":0};




let searchQuery = text;
const APP_ID = '10a11e73';
const APP_key = '0bb2267f6d318266de72f6b604eb58bc';
// console.log(container)

window.onload = () => {
    searchQuery = text;
    const baseurl = `https://api.edamam.com/search?q=${searchQuery}&app_id=${APP_ID}&app_key=${APP_key}&from=0&to=20`;
    fetchAPI(baseurl);
};



async function fetchAPI(baseURL) {
  
  const response = await fetch(baseURL);
  const data = await response.json();
  generateHTML(data.hits);
  console.log(data);
}

function generateHTML(results) {
  const searchBodyDiv = document.getElementById('search-results-body');
  let generatedHTML = "";
  results.map((result) => {
    generatedHTML += `
      <div class="item">
        <img src="${result.recipe.image}" alt="img">
        <div class="flex-container">
          <h1 class="title">${result.recipe.label}</h1>
          <a class="view-btn" target="_blank" href="${
            result.recipe.url
          }">View Recipe</a>
        </div>
        <p class="item-data">Calories per serving: ${(result.recipe.calories/result.recipe.yield).toFixed(2)}</p>
        <p class="item-data">Time: ${(result.recipe.totalTime>0?result.recipe.totalTime + ' minutes':"No Data Found")} </p>
        <p class="item-data">Diet Type: ${
          result.recipe.dietLabels.length > 0
            ? result.recipe.dietLabels 
            : "No Data Found"
        }</p>
        <p class="item-data">Ingredients: ${
          (result.recipe.ingredientLines+'').length>150? (result.recipe.ingredientLines+'').substr(0,150)+'...' : (result.recipe.ingredientLines +'')
        }</p>
      </div>
    `;
  });
  searchBodyDiv.innerHTML = generatedHTML;
}


function sortByCal(e){
  e = e || window.event;  
  let arg1 = e.target.getAttribute('data-arg1');
  let arg2 = e.target.getAttribute('data-arg2');
  let baseurl = `https://api.edamam.com/search?q=${searchQuery}&app_id=${APP_ID}&app_key=${APP_key}&from=0&to=20&calories=${arg1}-${arg2}`;
  //console.log(baseurl);
  fetchAPI(baseurl);
  
}
function sortByTime(e){
  e = e || window.event;  
  let arg1 = e.target.getAttribute('data-arg1');
  let arg2 = e.target.getAttribute('data-arg2');
  let baseurl = `https://api.edamam.com/search?q=${searchQuery}&app_id=${APP_ID}&app_key=${APP_key}&from=0&to=20&time=${arg1}-${arg2}`;
  //console.log(baseurl);
  fetchAPI(baseurl);
  
}
function sortByDiet(e){
  e = e || window.event;  
  let arg1 = e.target.getAttribute('data-arg1');
  let baseurl = `https://api.edamam.com/search?q=${searchQuery}&app_id=${APP_ID}&app_key=${APP_key}&from=0&to=20&diet=${arg1}`;
  //console.log(baseurl);
  fetchAPI(baseurl);
  
}

/*

window.onload = () => {
    loadTableData(data);
};


function loadTableData(tdata)
{
    const tablebody = document.getElementById('search-table');
    let htmldata= '';
    for (let row_data of  tdata){
        htmldata += `<tr><td  style="cursor:pointer" > <a  style="text-decoration:none" href= '${SERVER_URL}${row_data.page_link}'>${row_data.name}</a></td><td>${row_data.rating}</td><td>${row_data.cost}</td><td>${row_data.time}</td></tr>`;
        
    }
        
    console.log(htmldata);
    tablebody.innerHTML = htmldata;

}


function SortColumn(columnName)
{
    const dataType = typeof data[0][columnName];
    sort_decending = !sort_decending;
     console.log(dataType);
    switch(dataType)
    {
        case 'number':
            sortNumber(sort_decending, columnName) ;
            break;
        case 'string':
            sortString(sort_decending, columnName);
            break;
              
    }   
    loadTableData(data);
    console.log(data);
}
function SortColumnCost( columnName)
{
    
    sort_decending = !sort_decending;
    
    data = data.sort((p1, p2) => {
        return sort_decending? cost_dict[p1[columnName]]- cost_dict[p2[columnName]] : cost_dict[p2[columnName]]-cost_dict[p1[columnName]]
    });
    loadTableData(data);
    console.log(data);
}
function sortString(sort, columnName)
{
    data = data.sort((p1, p2) => {
        return sort?   p1[columnName].localeCompare(p2[columnName]) : p2[columnName].localeCompare(p1[columnName])
    });
}
function sortNumber(sort, columnName)
{
    data = data.sort((p1, p2) => {
        return sort? p1[columnName]- p2[columnName] : p2[columnName]-p1[columnName]
    });
}
*/