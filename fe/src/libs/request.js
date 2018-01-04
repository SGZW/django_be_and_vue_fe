import axios from 'axios';
import { Message } from 'iview';

function checkStatus (res) {
    if (res.status === 200 || res.status === 304) {
        return res;
    }

    const errorMsg = res.statusText || '请求或操作失败，请重试！';
    const error = new Error(errorMsg);
    error.res = res;

    throw error;
}

function checkAuth (res) {
    if (res && res.status_code !== 403) {
        return res;
    }

    const errorMsg = res.msg || '请求没有权限';
    const error = new Error(errorMsg);
    error.res = res;

    throw error;
}

function request (config) {
    return axios(config)
        .then(checkStatus)
        .then(res => res.data)
        .then(checkAuth)
        .catch(error => {
            Message.error(error.message);
        });
}

export default request;
