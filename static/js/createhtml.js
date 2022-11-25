function createLabel(lblname)
{
 
 var lbl = document.createElement("label");
 lbl.for = lblname;
 lbl.appendChild(document.createTextNode(lblname));
 
 return lbl;
}

function createInputText(name,id,typename)
{
         var txtfield = document.createElement("input");
            txtfield.type=typename;
            txtfield.name = name;
            txtfield.id = id;
			
			return txtfield;

}

function createDiv(id,classname)
{
   var div = document.createElement("div");
   div.id = id;
   div.className= classname;
   return div;
}

function createSelect(name,id,values)
{
	var selectfield = document.createElement("select");
	selectfield.id = id;
	selectfield.name = name;
	for(var i=0;i<values.length;i++)
	{
		var optfield = document.createElement("option");
		optfield.appendChild(document.createTextNode(values[i]));
		selectfield.appendChild(optfield);
	}
	return selectfield;
}

function createFormField(divclassname,lblname,txtname,typename)
{
	var divf = createDiv(null,divclassname);
	divf.appendChild(createLabel(lblname));
	
	divf.appendChild(createInputText(txtname,txtname,typename));
	
	
	return divf;
}
function createSelectFormField(divclassname,lblname,txtname,values)
{
	var divf = createDiv(null,divclassname);
	divf.appendChild(createLabel(lblname));
	divf.appendChild(createSelect(txtname,txtname,values));
	return divf;
}

function createForm()
{
	var form = document.getElementById("signup");
	var h2 = document.createElement("h1");
	h2.appendChild(document.createTextNode("SignUP"));
	form.appendChild(h2);
	form.appendChild(createFormField("form-field","FirstName","FirstName","Text"));
	form.appendChild(createFormField("form-field","LastName","LastName","Text"));
	form.appendChild(createFormField("form-field","JoinDate","JoinDate","date"));
	form.appendChild(createSelectFormField("form-field","Gender","Gender",['Male','Female']));
	form.appendChild(createSelectFormField("form-field","Skills","Skills",['C','CPP','DS','CoreJava','Oracle']));
	form.appendChild(createFormField("form-field","Password","Password","password"));
	form.appendChild(createFormField("form-field","","","submit"));
	
}
