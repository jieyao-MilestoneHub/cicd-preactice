import json

def pre_handler(event, context):
    """
    部屬前的 hook function。
    它可以在流量切換到新版本的 Lambda 函數之前執行某些操作。
    """
    print("Pre-deployment hook triggered")
    print(f"Event: {json.dumps(event)}")
    # 檢查配置、初始化資源等等
    return {
        'statusCode': 200,
        'body': json.dumps('Pre-deployment checks passed')
    }

def post_handler(event, context):
    """
    部屬後的 hook function。
    它可以在流量切換到新版本的 Lambda 函數之後執行某些操作。
    """
    print("Post-deployment hook triggered")
    print(f"Event: {json.dumps(event)}")
    # 紀錄日誌、清理資源
    return {
        'statusCode': 200,
        'body': json.dumps('Post-deployment tasks completed')
    }
