#[cfg(target_os = "macos")]
pub mod macos;

use crate::input::session::InputSink;
use std::io;

pub fn clipboard_backend() -> io::Result<Box<dyn crate::clipboard::Backend>> {
    #[cfg(target_os = "macos")]
    {
        crate::clipboard::native::create()
    }
    #[cfg(not(target_os = "macos"))]
    {
        Err(io::Error::new(
            io::ErrorKind::Unsupported,
            "此系统尚未实现剪贴板",
        ))
    }
}

pub fn input_sink() -> io::Result<Box<dyn InputSink>> {
    #[cfg(target_os = "macos")]
    {
        macos::input_simulation::MacInput::new().map(|sink| Box::new(sink) as Box<dyn InputSink>)
    }
    #[cfg(not(target_os = "macos"))]
    {
        Err(io::Error::new(
            io::ErrorKind::Unsupported,
            "input receiver is not implemented for this OS",
        ))
    }
}
