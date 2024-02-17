    #     # # 使用显式等待，等待评论加载完成
    #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'comment__text')))
        
    #     # # 提取评论元素
    #     comment_elements = driver.find_elements(By.CLASS_NAME, 'comment__text ')
        
    #     # # 打印评论文本
    #     for comment in comment_elements:
    #         print(comment.text)
    
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    