let util = {

};
util.title = function (title) {
    title = title ? title + ' - Home' : '派出所户籍管理系统';
    window.document.title = title;
};

util.languageCode = function () {
    return navigator.language || navigator.browserLanguage;
};

util.localName = function () {
    return '';
};

export default util;
