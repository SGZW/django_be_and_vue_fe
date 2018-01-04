// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import iView from 'iview';
import VueRouter from 'vue-router';
import VueI18n from 'vue-i18n';
import Util from '@/libs/util';
import router from '@/router/demo';
import App from './App.vue';
import store from '@/store';
import '@/themes/index.less';    // 使用 CSS

import zhLocale from 'iview/dist/locale/zh-CN';
import enLocale from 'iview/dist/locale/en-US';
import jaLocale from 'iview/dist/locale/ja-JP';
import ptLocale from 'iview/dist/locale/pt-BR';

Vue.config.productionTip = false;
Vue.config.debug = true;

Vue.use(VueRouter);
Vue.use(VueI18n);

// i18n support
const messages = {
    'zh-CN': zhLocale,
    'en-US': enLocale,
    'ja-JP': jaLocale,
    'pt-BR': ptLocale,
};

const i18n = new VueI18n({
    locale: Util.languageCode(),
    fallbackLocale: 'zh-CN',
    messages,
});

// fix vue-i18n 7.0
// see: https://github.com/iview/iview/issues/1090
Vue.use(iView, {
    i18n: function (path, options) {
        let value = i18n.t(path, options);
        if (value !== null && value !== undefined) {
            return value;
        }
        return '';
    },
});
// i18n support end

// loading bar
router.beforeEach((to, from, next) => {
    iView.LoadingBar.start();
    Util.title(to.meta.title);
    next();
});

router.afterEach((to, from, next) => {
    iView.LoadingBar.finish();
    window.scrollTo(0, 0);
});
// loading end

/* eslint-disable no-new */
new Vue({
    el: '#app',
    store,
    router,
    i18n,
    template: '<App/>',
    components: { App },
});
