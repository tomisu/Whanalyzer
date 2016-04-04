var days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday'];

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

function isInt(value) {
  return !isNaN(value) && 
         parseInt(Number(value)) == value && 
         !isNaN(parseInt(value, 10));
}

function dateFormat(date){
 return date.getDate() + '/'+ (date.getMonth() + 1) + '/' +  date.getFullYear()

}