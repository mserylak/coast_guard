import sqlalchemy as sa

# Create metadata object
metadata = sa.MetaData()

# Define the metadata object for the obsinfo table
sa.Table('obsinfo', metadata,
         sa.Column('object', sa.String(32), nullable=False),
         sa.Column('mjd', sa.Float(53), nullable=False),
         sa.Column('equinox', sa.Float, nullable=False),
         sa.Column('equinox_obs', sa.Float, nullable=False),
         sa.Column('exposuretime', sa.Float, nullable=False),
         sa.Column('projectid', sa.String(32), nullable=False),
         sa.Column('observer', sa.String(32), nullable=False),
         sa.Column('scan', sa.Integer, nullable=False),
         sa.Column('obstimestamp', sa.String(32), nullable=False),
         sa.Column('lst', sa.Float(53), nullable=False),
         sa.Column('nobs', sa.Integer, nullable=False),
         sa.Column('nsubs', sa.Integer, nullable=False),
         sa.Column('subsnum', sa.Integer, nullable=False),
         sa.Column('obsnum', sa.Integer, nullable=False),
         sa.Column('subfirstmjd', sa.Float(53), nullable=False),
         sa.Column('sublastmjd', sa.Float(53), nullable=False),
         sa.Column('ctype1', sa.String(32), nullable=False),
         sa.Column('ctype2', sa.String(32), nullable=False),
         sa.Column('wcsname', sa.String(32), nullable=False),
         sa.Column('lon', sa.Float, nullable=False),
         sa.Column('lat', sa.Float, nullable=False),
         sa.Column('longoff', sa.Float, nullable=False),
         sa.Column('latoff', sa.Float, nullable=False),
         sa.Column('scantype', sa.String(32), nullable=False),
         sa.Column('scanmode', sa.String(32), nullable=False),
         sa.Column('scandir', sa.String(8), nullable=False),
         sa.Column('scanlen', sa.Float, nullable=False),
         sa.Column('scanrot', sa.Float, nullable=False),
         sa.Column('scanxvel', sa.Float, nullable=False),
         sa.Column('nuseband', sa.Integer, nullable=False),
         sa.Column('nusefeed', sa.Integer, nullable=False),
         sa.Column('phases', sa.Integer, nullable=False),
         sa.Column('freqthrow', sa.Float, nullable=False),
         sa.Column('azcorr', sa.Float, nullable=False),
         sa.Column('elcorr', sa.Float, nullable=False),
         sa.Column('refraction', sa.Float, nullable=False),
         sa.Column('nula', sa.Float, nullable=False),
         sa.Column('nule', sa.Float, nullable=False),
         sa.Column('cols', sa.Float, nullable=False),
         sa.Column('linx', sa.Float, nullable=False),
         sa.Column('liny', sa.Float, nullable=False),
         sa.Column('linz', sa.Float, nullable=False),
         sa.Column('rotx', sa.Float, nullable=False),
         sa.Column('roty', sa.Float, nullable=False),
         sa.Column('rotz', sa.Float, nullable=False),
         sa.Column('temperature', sa.Float, nullable=False),
         sa.Column('pressure', sa.Float, nullable=False),
         sa.Column('humidity', sa.Float, nullable=False),
         sa.Column('windspeed', sa.Float, nullable=False),
         sa.Column('winddir', sa.Float, nullable=False),
         sa.Column('vlsr', sa.Float, nullable=False),
         sa.Column('vblsr', sa.Float, nullable=False),
         sa.Column('vhel', sa.Float, nullable=False),
         sa.Column('vbar', sa.Float, nullable=False),
         sa.Column('azim', sa.Float, nullable=False),
         sa.Column('elev', sa.Float, nullable=False),
         sa.Column('focus1', sa.Float, nullable=False),
         sa.Column('focus2', sa.Float, nullable=False),
         sa.Column('focus3', sa.Float, nullable=False),
         sa.Column('focus4', sa.Float, nullable=False),
         sa.Column('focus5', sa.Float, nullable=False),
         sa.Column('focus6', sa.Float, nullable=False),
         sa.Column('focus7', sa.Float, nullable=False),
         sa.Column('focus8', sa.Float, nullable=False),
         sa.Column('febe', sa.String(32), nullable=False),
         sa.Column('feversion', sa.String(32), nullable=False),
         sa.Column('ifinvert', sa.String(1), nullable=False),
         sa.Column('obstype', sa.String(32), nullable=False),
         sa.Column('scantime', sa.Float, nullable=False),
         sa.Column('scanxspacing', sa.Float, nullable=False),
         sa.Column('scanyspacing', sa.Float, nullable=False),
         sa.Column('scanskew', sa.Float, nullable=False),
         sa.Column('posgnp', sa.Float, nullable=False),
         sa.Column('dewang', sa.Float, nullable=False),
         sa.Column('channels', sa.Integer, nullable=False),
         sa.Column('freqres', sa.Float, nullable=False),
         sa.Column('bandwidth', sa.Float, nullable=False),
         sa.Column('molecule', sa.String(32), nullable=False),
         sa.Column('restfreq', sa.Float(53), nullable=False),
         sa.Column('sideband', sa.String(32), nullable=False),
         sa.Column('velwcsname', sa.String(32), nullable=False),
         sa.Column('velsys', sa.String(32), nullable=False),
         sa.Column('refchan', sa.Float, nullable=False),
         sa.Column('velrefchan', sa.Float, nullable=False),
         sa.Column('velchansep', sa.Float, nullable=False),
         sa.Column('velrestframe', sa.String(32), nullable=False),
         sa.Column('velobsframe', sa.String(32), nullable=False),
         sa.Column('velsource', sa.Float, nullable=False),
         sa.Column('velobserver', sa.Float, nullable=False),
         sa.Column('utc2ut1', sa.Float, nullable=False),
         sa.Column('tblank', sa.Float, nullable=False),
         sa.Column('tsync', sa.Float, nullable=False),
         sa.Column('dayofyear', sa.Integer, nullable=False),
         sa.Column('skyfreq', sa.Float(53), nullable=False),
         sa.Column('movefoc', sa.String(1), nullable=False),
         sa.Column('ctrlbuttons', sa.Integer, nullable=False),
         sa.Column('obsstatus', sa.String(8), nullable=False),
         mysql_engine='InnoDB', mysql_charset='ascii')