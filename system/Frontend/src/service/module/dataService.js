/*
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-11-20 19:23:35
 * @LastEditTime: 2022-11-22 17:18:36
 */

import axios from 'axios';

// axios.defaults.withCredentials = true
const TEST_URL_PREFIX = 'http://127.0.0.1:5000/api/test';

export function fetchHello(param, callback) {
    const url = `${TEST_URL_PREFIX}/hello/`;
    axios.post(url, param)
        .then(response => {
            callback(response.data)
        }, errResponse => {
            console.log(errResponse)
        })
}

export function uploadData(param, callback) {
    const url = `${TEST_URL_PREFIX}/upload/`;
    axios.post(url, param)
    .then(response => {
        callback(response.data);
    }, errResponse => {
        console.log(errResponse);
    })
}

export function fetchBasicChart(param, callback) {
    const url = `${TEST_URL_PREFIX}/fetchBasicChart/`;
    axios.post(url, param)
    .then(response => {
        callback(response);
    }, errResponse => {
        console.log(errResponse);
    })
}

export function postQuery(param, callback) {
    const url = `${TEST_URL_PREFIX}/postQuery/`;
    axios.post(url, param)
    .then(response => {
        callback(response);
    }, errResponse => {
        console.log(errResponse);
    });
}

export function getChat(param, callback) {
    const url = `${TEST_URL_PREFIX}/get_chat/`;
    axios.post(url, param)
    .then(response => {
        callback(response);
    }, errResponse => {
        console.log(errResponse);
    });

}