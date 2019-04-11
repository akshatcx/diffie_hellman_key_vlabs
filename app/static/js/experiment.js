var generatorvalue
var kA = 2
var kB = 3
var GA = 5
var GB = 9
var GAB = 3

var generatePrime = function()
{
   var primenumber = document.getElementById('primeno')
}

var nextGenerator = function()
{
  generatorvalue = document.getElementById('generator').value
}
var nextKeyA= function()
{
  Keybox1 = document.getElementById('keyA')
  Keybox1.value = kA;
}
var nextKeyB= function()
{
  Keybox2 = document.getElementById('keyB')
  Keybox2.value = kB;
}
function calculateGA()
{
  gabox = document.getElementById('encryptA')
  gabox.value=GA
}
function calculateGB()
{
  gabox = document.getElementById('encryptB')
  gabox.value=GB
}
function sendA()
{
  var recB = document.getElementById('receivedB')
  recB.value = GA
}
function sendB(){
  var recA = document.getElementById('receivedA')
  recA.value = GB
}
function calculateGAB(){
  var gabtext = document.getElementById('encryptAB')
  gabtext.value = GAB
}
function calculateGBA(){
  var gabtext = document.getElementById('encryptBA')
  gabtext.value = GAB
}
