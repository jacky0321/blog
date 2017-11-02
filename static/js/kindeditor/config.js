/**
 * Created by Administrator on 2017/3/11.
 */

KindEditor.ready(function(K) {
            K.create(' textarea[name=content]', {
            width:500,
            height:200,
                uploadJson: '/admin/upload/kindeditor',
        });
    });
