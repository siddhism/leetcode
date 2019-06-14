# get splan from admin signup data or 
# splan = 'CUSTOM_PLAN'
plan_kwargs = {'company': company,
 'country': None,
 'plan': splan,
 'timezone': None}
CompanySubscription.create_or_update_company_subscription(
            **plan_kwargs)