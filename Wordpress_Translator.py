from googletrans import Translator
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods.posts import GetPosts, EditPost
#logs into wordpress_xmlrpc
def UserInput():
    return {"url": input("Please provide URL: "),
    "username": input("Please provide Username: "),
    "password": input("Please provide Password: "),
    "lang_src": input("Please provide language of site: "),
    "lang_dest": input("Please provide desired language to translate to: ")}

def TranslateList(items):
    a = []
    for i in items:
        a.append(Translate(i))
    return a
#translates lists to selected language
def TranslateLong(text, split_by="\n"):
    text_list = text.split(split_by)
    translated_text = ""
    for sentence in text_list:
        if len(sentence) == 0 or sentence == None:
            break
        if split_by == "\n":
            translated_text += "\n" + Translate(sentence)
        else:
            translated_text += " " + Translate(sentence + split_by)
    return translated_text
#translates post to selected language
def TranslatePost(post):
    if post.title != None and post.title != " " and len(post.title) != 0:
        try:
            post.title = Translate(post.title)
        except:
            try:
                post.title = translator.translate(post.title).text
            except:
                error.append([post.id,"Title"])
                error_file.write("Title, " + post.id)
    try:
        post.content = Translate(post.content)
    except:
        try:
            post.content = TranslateLong(post.content)
        except:
            try:
                post.content = TranslateLong(post.content, split_by="!")
            except:
                try:
                    post.content = TranslateLong(post.content, split_by="?")
                except:
                    try:
                        post.content = TranslateLong(post.content, split_by=".")
                    except:
                        error.append([post.id, "content"])
                        error_file.write("Content, " + post.id)
    try:
        post.terms_names["post_tag"] = TranslateList(post.terms_names["post_tag"])
    except:
        pass
    try:
        post.terms_names["category"] = TranslateList(post.terms_names["category"])
    except:
        pass
    return post
#Translates All posts to english
def TranslateBatchPosts(batch_posts):
    for post in batch_posts:
        translated_post = TranslatePost(post)
        try:
            wp.call(EditPost(translated_post.id, translated_post))
            print("Uploaded: " + translated_post.id)
        except:
            try:
                post.thumbnail=post.thumbnail['attachment_id']
                wp.call(EditPost(translated_post.id, translated_post))
                print("Uploaded: " + translated_post.id)
            except:
                error.append([post.id, "upload"])
                error_file.write("Upload, " + translated_post.id)

if __name__ == "__main__":
    #Gets User Input
    user_data = UserInput()
    wp = Client(user_data["url"] + "/xmlrpc.php", user_data["username"], user_data["password"])
    #The class which has translate function
    translator = Translator()
    error_file = open("error.txt", "w")
    error = []
    #translates to english
    Translate = lambda text: translator.translate(text, src=user_data["lang_src"], dest=user_data["lang_dest"]).text
    #translates posts in batches of 20
    offset = 0
    increment = 20
    while True:
            print(offset)
            posts = wp.call(GetPosts({'number': increment, 'offset': offset}))
            if len(posts) == 0:
                    break  # no more posts returned
            print("Error: " + str(len(error)))
            TranslateBatchPosts(posts)
            offset += increment
    print(error)
    error_file.close()
