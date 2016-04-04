//Only takes in count the first instance of an index

function uniqueAdd(uIndex){
		return function(p,d){
			if ( d[uIndex] in p.publicaciones ){
				p.publicaciones[d[uIndex]]++;		
				
			} else{
				p.publicaciones[d[uIndex]] = 1;
                p.count++;
			}
	        return p;
		}

	}

function uniqueRemove(uIndex){
	return function (p, d) {
    	p.publicaciones[d[uIndex]]--;
        if (p.publicaciones[d[uIndex]] === 0) {
            delete p.publicaciones[d[uIndex]];
            p.count--;
        }
        return p;
    }
}

function uniqueInit(){
	return  function () {
				return {
					count:0,
					publicaciones: {
						/*
						id: 1 //id en cuestión
						count: 5 //veces que está esa id
						*/
					}
				};
		    }
}




function allAdd(p, v) {
	return function(p, v){
		  counsole.log(v);
		  return p;
	}

}

function allRemove(p, v) {
	return function(p, v){

	}
   //omitted. not useful for demonstration
}

function allInitial() {
	return function(){
		return {};  
	}
  
}