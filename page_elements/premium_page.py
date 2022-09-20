from selenium.webdriver.common.by import By


class PremiumPage:
    PREMIUM_LANDING = {
        'text_privilege': (By.XPATH, '//section[@data-widget="premiumLandingWelcomeNonPremium"]//span'),
        'button': (By.XPATH, '//section[@data-widget="premiumLandingWelcomeNonPremium"]//a/div')
    }
