const name = "Jesse";
const age = 40;
const message = () => {
const name = "Jesse";
const age = 40;
return name + ' is ' + age + ' years old.';
};

export class Student
{
	constructor(rno,name,course,fee) // constructor method
	{
		this.rno = rno;
		this.name = name;
		this.course = course;
		this.fee = fee;
	}
	
	
}
export default message;
export {name, age};