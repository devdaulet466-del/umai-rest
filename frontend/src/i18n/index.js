import { createI18n } from 'vue-i18n'

import en from './locales/en.json'
import ru from './locales/ru.json'
import kk from './locales/kk.json'

const getBrowserLang = () => {
    // navigator.language can be 'en-US', 'ru-RU', etc.
    const browserLang = navigator.language || navigator.userLanguage
    if (browserLang.startsWith('ru')) return 'ru'
    if (browserLang.startsWith('kk')) return 'kk'
    return 'en' // fallback
}

const i18n = createI18n({
    legacy: false, // you must set `false`, to use Composition API
    locale: getBrowserLang(), // set locale dynamically based on browser

    fallbackLocale: 'en', // set fallback locale
    messages: {
        en,
        ru,
        kk
    }
})

export default i18n
