// ==UserScript==
// @name         Jufe auto select the course
// @namespace    http://tampermonkey.net/

// @version      0.1
// @description  select the course!
// @author       ----
// @match        http://tampermonkey.net/documentation.php?ext=dhdg

// @grant        unsafeWindow

// @include      http://172.31.5.68/lightSelectSubject/


// @include      http://172.31.5.74/lightSelectSubject/

// @include      http://172.31.5.75/lightSelectSubject/



// @include      http://172.31.5.77/lightSelectSubject/

// @include      http://172.31.5.78/lightSelectSubject/

// @include      http://172.29.5.137/lightSelectSubject/

// @include      http://172.31.5.76/lightSelectSubject/

// @include      http://172.29.5.139/lightSelectSubject/

// @include      http://172.29.5.244/lightSelectSubject/

// @include      http://172.29.5.246/lightSelectSubject/

// @include      http://172.29.5.248/lightSelectSubject/

// @include      http://172.31.5.139/lightSelectSubject/

// @include      http://172.31.5.195/lightSelectSubject/

// @include      http://218.87.6.200/lightSelectSubject/

// @include      http://172.31.5.223/lightSelectSubject/

// @include      https://ssl.jxufe.edu.cn/cas/login*


// auto login to jufe 信息门户
//code = document.getElementsByTagName('input');
//    for (var i=0;i<code.length;i++)
//{
//    if (code[i].type === 'submit'){
//     code[i].click();
//    }
//}


// @run-at       document-end
// ==/UserScript==

(function() {
    'use strict';

    // Your code here...
    // 自动填充用户名和密码，并且自动点击获取验证码
    var username, password, code;
    username = document.getElementById('username');
    password = document.getElementById('password');
    username.value = '2201702841';
    password.value = 'jkl147258';
    code = document.getElementById('signBtn');
    code.click();

})();
