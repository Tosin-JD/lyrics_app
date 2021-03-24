from django import forms

from .models import Lyric, Chorus, Verse, Bridge

class LyricForm(forms.ModelForm):
    """A form for creating new lyrics."""
    
    def __init__(self, *args, **kwargs):
        super(LyricForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control mb-1'
        self.fields['song_writer'].widget.attrs['class'] = 'form-control mb-1'
        
    class Meta:
        model = Lyric
        fields = ('title', 'song_writer', )
    
    
    
    
        
        


