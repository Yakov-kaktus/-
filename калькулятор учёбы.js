var a = 2;
while (True){
  var a += 1;
  if (a == 2){
    console.log('отчислен')
    break
  } else if (a == 3) {
    console.log('терпимо/можн пересдать')
    continue 
  } else if (a == 4) {
    console.log('норм')
  } else if (a == 5) {
    console.log('хорошо')
    break
  }
}
