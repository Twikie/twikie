import cloudfiles

def upload_cloud_file( fd, user, project, page, revision ):
    cloud_user = 'nthomson'
    cloud_key = '6b87156a72dc5c3e1d1b4943a8b0e238'
    cloud_container = 'images'
    
    connection = cloudfiles.get_connection(cloud_user, cloud_key)
    container = connection.get_container(cloud_container)
    
    #open a file and write the descriptor
    ob = container.create_object('%s_%s_%s_%s_%s' % (user, project, page, revision, fd.name) )
    ob.content_type = fd.content_type
    for chunk in fd.chunks():
        ob.write(chunk)
    fd.close()
    return ob.public_uri()
