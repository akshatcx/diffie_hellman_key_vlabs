var primenumber = document.getElementById('primeno')
var generatorvalue = document.getElementById('generator')
var Keybox1 = document.getElementById('keyA')
var Keybox2 = document.getElementById('keyB')
var gabox = document.getElementById('encryptA')
var gbbox = document.getElementById('encryptB')
var recB = document.getElementById('receivedB')
var recA = document.getElementById('receivedA')
var gabtext = document.getElementById('encryptAB')
var gabtext = document.getElementById('encryptBA')


function generatePrime()
{
    if (primenumber.value==""){
        fetch("/api/genp?bits=256")
            .then((res) => res.json())
            .then(res => {
                primenumber.value=res.prime
            });
    }
}

function nextGenerator(){

  if (generatorvalue.value=""){
    fetch("/api/geng/?bits=256")
      .then((res) => res.json())
      .then(res => {
        generatorvalue.value=res.generator
      });
  }
}
function nextKeyA()
{
  if (Keybox1.value=""){
    fetch("/api/private_key/?prime="+primenumber.value)
      .then((res) => res.json())
      .then(res => {
      Keybox1.value=res.private_key
      });
    }
}
function nextKeyB()
{
  if (Keybox2.value=""){
    fetch("/api/private_key/?prime="+primenumber.value)
      .then((res) => res.json())
      .then(res => {
        Keybox2.value=res.private_key
      });
  }
}

function calculateGA()
{
  fetch("/api/calg/?p="+primenumber.value+"&a="+Keybox1.value+"&b="+Keybox2.value+"&g="+generatorvalue.value)
      .then((res) => res.json())
      .then(res => {
        gabox.value=res.Ga
      });
}
function calculateGB()
{
  fetch("/api/calg/?p="+primenumber.value+"&a="+Keybox1.value+"&b="+Keybox2.value+"&g="+generatorvalue.value)
      .then((res) => res.json())
      .then(res => {
        gbbox.value=res.Gb
      });
}
function sendA()
{
  fetch("/api/calg/?p="+primenumber.value+"&a="+Keybox1.value+"&b="+Keybox2.value+"&g="+generatorvalue.value)
      .then((res) => res.json())
      .then(res => {
        recB.value=res.Ga
      });
}
function sendB(){
  fetch("/api/calg/?p="+primenumber.value+"&a="+Keybox1.value+"&b="+Keybox2.value+"&g="+generatorvalue.value)
      .then((res) => res.json())
      .then(res => {
        recB.value=res.Gb
      });
}
function calculateGAB(){
  fetch("/api/calg/?p="+primenumber.value+"&a="+Keybox1.value+"&b="+Keybox2.value+"&g="+generatorvalue.value)
      .then((res) => res.json())
      .then(res => {
        gabtext.value=res.Gab
      });
}
function calculateGBA(){
  fetch("/api/calg/?p="+primenumber.value+"&a="+Keybox1.value+"&b="+Keybox2.value+"&g="+generatorvalue.value)
      .then((res) => res.json())
      .then(res => {
        gabtext.value=res.Gba
      });
}
